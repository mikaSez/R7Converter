package info.mikasez.generators;


import info.mikasez.generators.matchers.TagMatcher;
import info.mikasez.models.Element;

/**
 * Generates a String in specified textFormat <br>
 * The text format is produced from the matcher.
 */
public class Generator {
    private Element root;


    public Generator(Element root, TagMatcher matcher) {

        this.root = root;
        this.root.setTagMatcher(matcher);

    }

    public String generate() {
        return root.generate();
    }
}
