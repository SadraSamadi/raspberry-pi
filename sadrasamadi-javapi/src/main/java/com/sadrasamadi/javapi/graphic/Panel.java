package com.sadrasamadi.javapi.graphic;

public abstract class Panel {

    protected int width;

    protected int height;

    public Panel(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public abstract void render(Canvas canvas, float delta);

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

}
