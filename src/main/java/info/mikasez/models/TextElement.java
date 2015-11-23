package info.mikasez.models;

/**
 * Only text representation <br>
 * This element cannot have any children
 */
public class TextElement extends Element {
    String value;

    public TextElement(DocType type, String text) {
        super(type);
        this.value = text;

    }


    @Override
    public String generate() {
        return value;
    }
}
