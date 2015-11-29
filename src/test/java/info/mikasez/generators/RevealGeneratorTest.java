package info.mikasez.generators;

import info.mikasez.generators.matchers.RevealTagMatcher;
import info.mikasez.models.DocType;
import info.mikasez.models.Element;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * Created by MikaSez on 29/11/2015.
 */
public class RevealGeneratorTest {
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


        element.addChild(h);
        element.addChild(h2);
        element.addChild(p);

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

        element.addChild(list);


        tested = new Generator(element, new RevealTagMatcher());
    }


    @Test
    public void generateTest() {
        StringBuilder sb = new StringBuilder();
        sb.append("<!doctype html>\n" +
                "<html lang=\"en\">\n" +
                "<head>\n" +
                "<meta charset=\"utf-8\">\n" +
                "<title>reveal.js - Barebones</title>\n" +
                "<link rel=\"stylesheet\" href=\"http://lab.hakim.se/reveal-js/css/reveal.css\">\n" +
                "</head>\n" +
                "<body>\n" +
                "<div class=\"reveal\">\n" +
                "<div class=\"slides\">\n" +
                "<h1>Header1</h1>\n" +
                "\n" +
                "<h2>Header2</h2>\n" +
                "\n" +
                "<p>On July 2, <em>an alien mothership</em> entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide.</p>\n" +
                "\n" +
                "<ul>\n" +
                "</li>Item 1</li>\n" +
                "\n" +
                "</li>Item 2</li>\n" +
                "\n" +
                "</li>Item 3</li>\n" +
                "</ul>\n" +
                "</div>\n" +
                "</div>\n" +
                "<script src=\"http://lab.hakim.se/reveal-js/js/reveal.js\"></script>\n" +
                "<script>\n" +
                "Reveal.initialize();\n" +
                "</script>\n" +
                "</body>\n" +
                "</html>");
        Assert.assertEquals(sb.toString(), tested.generate());
    }
}
