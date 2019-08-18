package com.sadrasamadi.javapi;

import com.sadrasamadi.javapi.graphic.Canvas;
import com.sadrasamadi.javapi.graphic.Graphic;
import com.sadrasamadi.javapi.graphic.Panel;

public class MyPanel extends Panel {

    private float x = 0;

    private float y = 0;

    private float vx = 5;

    private float vy = 5;

    public MyPanel() {
        super(Graphic.WIDTH, Graphic.HEIGHT);
    }

    @Override
    public void render(Canvas canvas, float delta) {
        canvas.clear();
        for (int i = 0; i < width; i++) {
            canvas.on(i, 0);
            canvas.on(i, height - 1);
        }
        for (int i = 1; i < height - 1; i++) {
            canvas.on(0, i);
            canvas.on(width - 1, i);
        }
        canvas.drawDot(x, y);
        x += vx * delta;
        y += vy * delta;
        if (x <= 1)
            vx = Math.abs(vx);
        if (x >= width - 2)
            vx = -Math.abs(vx);
        if (y <= 1)
            vy = Math.abs(vy);
        if (y >= height - 2)
            vy = -Math.abs(vy);
    }

}
