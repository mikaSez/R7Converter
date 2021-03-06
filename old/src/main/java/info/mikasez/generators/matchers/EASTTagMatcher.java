package info.mikasez.generators.matchers;

import info.mikasez.models.DocType;

/**
 * Created by MikaSez on 29/11/2015.
 */
public class EASTTagMatcher implements TagMatcher {
    @Override
    public String getPostTag(DocType type) {
        switch (type) {
            case Table:
                return "\n</TABLES>";
            case TabHeaderElement:
                return "\n</TAB_ENTETE>";
            case TabBodyElement:
                return "\n</TAB_CORPS>";
            case Root:
                return "\n</EAST>";
            case Header1:
            case Header2:
                return "\n</TITRE>\n";
            case List:
                return "\n</LISTE>";
            case ListElement:
                return "</EL>\n";
            case Emphasis:
                return "</EMPHASE> ";
            case Slide:
                return "\n</SECTION>\n";
            case Paragraph:
                return "\n</PARAGRAPH>\n";
            default:
                return "";
        }
    }

    @Override
    public String getPreTag(DocType type) {
        switch (type) {
            case Table:
                return "<TABLES>\n";
            case TabHeaderElement:
                return "<TAB_ENTETE>\n";
            case TabBodyElement:
                return "<TAB_CORPS>\n";
            case Root:
                return "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><EAST transition=\"burst\">\n" +
                        "<PREFERENCES>\n" +
                        "<AFFICHAGE>\n" +
                        "<POLICE_TEXTE font=\"Comic Sans MS\"/>\n" +
                        "</AFFICHAGE>\n" +
                        "</PREFERENCES>";
            case Header1:
            case Header2:
                return "\n<TITRE>\n";
            case List:
                return "<LISTE couleur_puce=\"green\" type=\"square\">\n";
            case ListElement:
                return "<EL>";
            case Emphasis:
                return " <EMPHASE>";
            case Paragraph:
                return "\n<PARAGRAPH>\n";
            case Slide:
                return "\n<SECTION>\n";
            default:
                return "";
        }
    }
}
