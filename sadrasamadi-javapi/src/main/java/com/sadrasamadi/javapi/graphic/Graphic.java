package com.sadrasamadi.javapi.graphic;

import com.pi4j.io.gpio.*;

import java.util.ArrayList;
import java.util.List;

public class Graphic {

    public static final int WIDTH = 12;

    public static final int HEIGHT = 9;

    private static final long NS_PER_RENDER = 5_000;

    private static final int FRAME_PER_SECOND = 60;

    private static final long NS_PER_FRAME = Math.round(1_000_000_000f / FRAME_PER_SECOND);

    private int width;

    private int height;

    private boolean running;

    private Panel panel;

    private Canvas canvas;

    private List<GpioPinDigitalOutput> coms;

    private List<GpioPinDigitalOutput> segs;

    private Thread renderThread;

    private Thread updateThread;

    public Graphic(Panel panel) {
        this.panel = panel;
        width = panel.getWidth();
        height = panel.getHeight();
        if (width < 0 || width > Graphic.WIDTH || height < 0 || height > Graphic.HEIGHT)
            throw new IllegalArgumentException("panel size is not supported");
        running = true;
        canvas = new Canvas(width, height);
        coms = gpioPinDigitalOutputList(
                RaspiPin.GPIO_08,
                RaspiPin.GPIO_09,
                RaspiPin.GPIO_07,
                RaspiPin.GPIO_00,
                RaspiPin.GPIO_02,
                RaspiPin.GPIO_03,
                RaspiPin.GPIO_12,
                RaspiPin.GPIO_13,
                RaspiPin.GPIO_14
        );
        segs = gpioPinDigitalOutputList(
                RaspiPin.GPIO_15,
                RaspiPin.GPIO_16,
                RaspiPin.GPIO_01,
                RaspiPin.GPIO_04,
                RaspiPin.GPIO_05,
                RaspiPin.GPIO_06,
                RaspiPin.GPIO_10,
                RaspiPin.GPIO_11,
                RaspiPin.GPIO_26,
                RaspiPin.GPIO_27,
                RaspiPin.GPIO_28,
                RaspiPin.GPIO_29
        );
    }

    private List<GpioPinDigitalOutput> gpioPinDigitalOutputList(Pin... pins) {
        ArrayList<GpioPinDigitalOutput> list = new ArrayList<>();
        GpioController gpio = GpioFactory.getInstance();
        for (Pin pin : pins) {
            GpioPinDigitalOutput gpioPinDigitalOutput = gpio.provisionDigitalOutputPin(pin);
            list.add(gpioPinDigitalOutput);
        }
        return list;
    }

    private void render() {
        boolean[][] matrix = canvas.getMatrix();
        while (running) {
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    GpioPinDigitalOutput seg = segs.get(j);
                    seg.setState(!matrix[i][j]);
                }
                GpioPinDigitalOutput com = coms.get(i);
                com.high();
                sleep(NS_PER_RENDER);
                com.low();
            }
        }
    }

    private void update() {
        long last = System.nanoTime();
        while (running) {
            long current = System.nanoTime();
            long elapsed = current - last;
            panel.render(canvas, elapsed / 1_000_000_000f);
            last = current;
            sleep(Graphic.NS_PER_FRAME);
        }
    }

    public void start() {
        coms.forEach(GpioPinDigitalOutput::low);
        segs.forEach(GpioPinDigitalOutput::high);
        renderThread = new Thread(this::render);
        renderThread.setPriority(Thread.MAX_PRIORITY);
        updateThread = new Thread(this::update);
        updateThread.setPriority(Thread.MIN_PRIORITY);
        renderThread.start();
        updateThread.start();
    }

    public void stop() {
        try {
            running = false;
            renderThread.join();
            updateThread.join();
            renderThread = null;
            updateThread = null;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @SuppressWarnings("StatementWithEmptyBody")
    private static void sleep(long ns) {
        long target = System.nanoTime() + ns;
        while (target > System.nanoTime()) ;
    }

}
