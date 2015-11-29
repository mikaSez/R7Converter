package info.mikasez.generators.matchers;

import info.mikasez.models.DocType;

/**
 * This class define matches between internal format and MarkDown format
 */
public class MDTagMatcher implements TagMatcher {


    @Override
    public String getPostTag(DocType type) {
        switch (type) {
            case Emphasis:
                return "* ";
            case StrongEmphasis:
                return "** ";
            case OneLineCode:
                return "` ";
            case Root:
                return "";
            default:
                return "\n";
        }

    }

    @Override
    public String getPreTag(DocType type) {
        switch (type) {
            case Paragraph:
                return "";
            case Header1:
                return "# ";
            case Header2:
                return "## ";
            case Header3:
                return "### ";
            case Header4:
                return "####";
            case Header5:
                return "#####";
            case Header6:
                return "######";
            case List:
                return "";
            case ListElement:
                return "* ";
            case BlockQuote:
                return "> ";
            case Emphasis:
                return " *";
            case StrongEmphasis:
                return " **";
            case OneLineCode:
                return " `";
            default:
                return "";
        }
    }
}
