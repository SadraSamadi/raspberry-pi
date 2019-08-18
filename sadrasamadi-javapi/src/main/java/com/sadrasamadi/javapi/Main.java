package com.sadrasamadi.javapi;

import com.sadrasamadi.javapi.graphic.Graphic;

public class Main {

    @SuppressWarnings("InfiniteLoopStatement")
    public static void main(String[] args) throws Exception {
        MyPanel panel = new MyPanel();
        Graphic graphic = new Graphic(panel);
        graphic.start();
        Runtime runtime = Runtime.getRuntime();
        Thread shutdownHook = new Thread(graphic::stop);
        runtime.addShutdownHook(shutdownHook);
        while (true)
            Thread.sleep(500);
    }

}
