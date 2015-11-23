package info.mikasez.models;

import info.mikasez.generators.matchers.TagMatcher;

import java.util.ArrayList;
import java.util.List;

/**
 * Element used for java representation of file formats.
 */
public class Element {
    private DocType type;
    private List<Element> children;
    private TagMatcher matcher;


    public Element(DocType type) {
        this.type = type;
        children = new ArrayList<>();
    }

    /**
     * @return the added children
     */
    public Element addChild(Element child) {
        children.add(child);
        return child;
    }


    /**
     * Adds a new text node
     *
     * @return the added children
     */
    public Element addTextChild(String child) {
        Element c = new TextElement(DocType.Text, child);
        children.add(c);
        return c;
    }

    public DocType getType() {
        return this.type;
    }

    /**
     *
     * */
    public void setTagMatcher(TagMatcher matcher) {
        this.matcher = matcher;
    }

    public String generate() {
        assert (matcher != null) : "Missing TagMatcher, use setTagMatcher before generating";
        StringBuilder sb = new StringBuilder();
        sb.append(GeneratePreTag());
        children.forEach(s -> {
            s.setTagMatcher(this.matcher);
            sb.append(s.generate());
        });
        sb.append(GeneratePostTag());

        return sb.toString();

    }

    /**
     * @return The closing tag for the current textFormat <br>
     * If no tag specified for given format returns empty String
     */
    private String GeneratePostTag() {
        return matcher.getPostTag(this.getType());
    }

    /**
     * @return The oppening tag for current textFormat <br>
     * If no tag specified returns empty String
     */
    private String GeneratePreTag() {
        return matcher.getPreTag(this.getType());
    }

}
