package info.mikasez.generators.matchers;

import info.mikasez.models.DocType;

/**
 * Created by MikaSez on 29/11/2015.
 */
public class RevealTagMatcher implements TagMatcher {
    @Override
    public String getPostTag(DocType type) {
        switch (type) {
            case Paragraph:
                return "</p>\n";
            case Header1:
                return "</h1>\n";
            case Header2:
                return "</h2>\n";
            case Header3:
                return "</h3>\n";
            case Header4:
                return "</h4>\n";
            case Header5:
                return "</h5>\n";
            case Header6:
                return "</h6>\n";
            case List:
                return "</ul>\n";
            case ListElement:
                return "</li>\n";
            case BlockQuote:
                return "</blockquote>\n";
            case Emphasis:
                return "</em> ";
            case StrongEmphasis:
                return "</strong> ";
            case OneLineCode:
                return "</code> ";
            case Root:
                return "</div>\n" +
                        "</div>\n" +
                        "<script src=\"http://lab.hakim.se/reveal-js/js/reveal.js\"></script>\n" +
                        "<script>\n" +
                        "Reveal.initialize();\n" +
                        "</script>\n" +
                        "</body>\n" +
                        "</html>";
            default:
                return "";
        }
    }

    @Override
    public String getPreTag(DocType type) {
        switch (type) {
            case Paragraph:
                return "\n<p>";
            case Header1:
                return "\n<h1>";
            case Header2:
                return "\n<h2>";
            case Header3:
                return "\n<h3>";
            case Header4:
                return "\n<h4>";
            case Header5:
                return "\n<h5>";
            case Header6:
                return "\n<h6>";
            case List:
                return "\n<ul>";
            case ListElement:
                return "\n</li>";
            case BlockQuote:
                return "\n<blockquote>";
            case Emphasis:
                return " <em>";
            case StrongEmphasis:
                return " <strong>";
            case OneLineCode:
                return " <code>";
            case Root:
                return "<!doctype html>\n" +
                        "<html lang=\"en\">\n" +
                        "<head>\n" +
                        "<meta charset=\"utf-8\">\n" +
                        "<title>reveal.js - Barebones</title>\n" +
                        "<link rel=\"stylesheet\" href=\"http://lab.hakim.se/reveal-js/css/reveal.css\">\n" +
                        "</head>\n" +
                        "<body>\n" +
                        "<div class=\"reveal\">\n" +
                        "<div class=\"slides\">";

            default:
                return "";
        }
    }
}
