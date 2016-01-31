package info.mikasez.processors.properties;

import info.mikasez.processors.FileProcessor;
import info.mikasez.processors.exception.ProcessException;

import java.util.regex.Pattern;

/**
 * Processor for MD properties files.
 */
public class MdProcessor implements FileProcessor {
    private final static String Paragraphe = "\\w+";
    private final static String Header = "^#{1,6}\\s";
    private final static String Blockquote = "^>\\s";
    private final static String Emphasis = "\\*\\w+\\*";
    private final static String StrongEmphasis = "\\*\\*\\w+\\*\\*";
    private final static String UnoderedList = "^[\\*-]\\s";
    private final static String OrderedList = "\\d\\p{Punct}";
    private final static String CodeBlock = "^`{3}";
    private final static String Code = "`\\w`";


    private final static String multiline = "(^#{1,6}\\s)|(^>\\s)|(^[\\*-]\\s)|(\\d\\p{Punct})|(^`{3})";

    public static boolean isMultiline(String r) {
        return !Pattern.matches(multiline, r);
    }

    @Override
    public void process(String line) throws ProcessException {

    }
}
