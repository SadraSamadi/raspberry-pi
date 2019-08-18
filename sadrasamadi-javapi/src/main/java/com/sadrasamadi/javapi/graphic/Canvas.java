package com.sadrasamadi.javapi.graphic;

public class Canvas {

    private int width;

    private int height;

    private boolean[][] matrix;

    public Canvas(int width, int height) {
        this.width = width;
        this.height = height;
        matrix = new boolean[height][width];
        setAll(false);
    }

    public void set(float x, float y, boolean state) {
        int rx = Math.round(x);
        int ry = Math.round(y);
        if (rx >= 0 && rx < width && ry >= 0 && ry < height)
            matrix[ry][rx] = state;
    }

    public void on(float x, float y) {
        set(x, y, true);
    }

    public void off(float x, float y) {
        set(x, y, false);
    }

    public void setAll(boolean state) {
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                matrix[i][j] = state;
    }

    public void onAll() {
        setAll(true);
    }

    public void offAll() {
        setAll(false);
    }

    public void clear() {
        offAll();
    }

    public void fill() {
        onAll();
    }

    public void inverse() {
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                matrix[i][j] = !matrix[i][j];
    }

    public void drawDot(float x, float y) {
        on(x, y);
    }

    public boolean[][] getMatrix() {
        return matrix;
    }

}
