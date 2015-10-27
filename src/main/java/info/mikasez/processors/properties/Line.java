package info.mikasez.processors.properties;

/**
 * Created by MikaSez on 15/10/2015.
 */
public class Line {
    private boolean oneline;
    private String line;


    public Line(boolean b, String s) {
        oneline = b;
        line = s;
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Line line1 = (Line) o;

        if (oneline != line1.oneline) return false;
        return !(line != null ? !line.equals(line1.line) : line1.line != null);

    }

    @Override
    public int hashCode() {
        int result = (oneline ? 1 : 0);
        result = 31 * result + (line != null ? line.hashCode() : 0);
        return result;
    }

    @Override
    public String toString() {
        return "Line{" +
                "oneline=" + oneline +
                ", line='" + line + '\'' +
                '}';
    }
}
