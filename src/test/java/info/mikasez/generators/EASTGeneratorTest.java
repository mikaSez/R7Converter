package info.mikasez.generators;

import info.mikasez.generators.matchers.EASTTagMatcher;
import info.mikasez.models.DocType;
import info.mikasez.models.Element;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * Created by MikaSez on 29/11/2015.
 */
public class EASTGeneratorTest {
    private Generator tested;


    @Before
    public void setUp() {
        Element element = new Element(DocType.Root);
        Element p = new Element(DocType.Paragraph);
        p.addTextChild("On July 2,");
        Element ocode = new Element(DocType.Emphasis);
        ocode.addTextChild("an alien mothership");
        p.addChild(ocode);
        p.addTextChild("entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide.");
        Element h = new Element(DocType.Header1);
        h.addTextChild("Header1");
        Element h2 = new Element(DocType.Header2);

        h2.addTextChild("Header2");

        Element slide1 = new Element(DocType.Slide);

        slide1.addChild(h);
        slide1.addChild(h2);
        element.addChild(slide1);

        Element slide2 = new Element(DocType.Slide);
        slide2.addChild(p);

        element.addChild(slide2);

        Element list = new Element(DocType.List);

        Element lc1 = new Element(DocType.ListElement);
        lc1.addTextChild("Item 1");
        list.addChild(lc1);
        Element lc2 = new Element(DocType.ListElement);
        lc2.addTextChild("Item 2");
        list.addChild(lc2);
        Element lc3 = new Element(DocType.ListElement);
        lc3.addTextChild("Item 3");
        list.addChild(lc3);


        Element slide3 = new Element(DocType.Slide);
        slide3.addChild(list);
        element.addChild(slide3);


        tested = new Generator(element, new EASTTagMatcher());
    }


    @Test
    public void generateTest() {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><EAST transition=\"burst\">\n" +
                "<PREFERENCES>\n" +
                "<AFFICHAGE>\n" +
                "<POLICE_TEXTE font=\"Comic Sans MS\"/>\n" +
                "</AFFICHAGE>\n" +
                "</PREFERENCES>\n" +

                "<SECTION>\n" +
                "\n" +
                "<TITRE>\n" +
                "Header1\n" +
                "</TITRE>\n" +
                "\n" +
                "<TITRE>\n" +
                "Header2\n" +
                "</TITRE>\n" +
                "\n" +
                "</SECTION>\n" +
                "\n" +
                "<SECTION>\n" +
                "\n" +
                "<PARAGRAPH>\n" +
                "On July 2, <EMPHASE>an alien mothership</EMPHASE> entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide.\n" +
                "</PARAGRAPH>\n" +
                "\n" +
                "</SECTION>\n" +
                "\n" +
                "<SECTION>\n" +
                "<LISTE couleur_puce=\"green\" type=\"square\">\n" +
                "<EL>Item 1</EL>\n" +
                "<EL>Item 2</EL>\n" +
                "<EL>Item 3</EL>\n" +
                "\n" +
                "</LISTE>\n" +
                "</SECTION>\n" +
                "\n" +
                "</EAST>");
        Assert.assertEquals(sb.toString(), tested.generate());
    }
}
