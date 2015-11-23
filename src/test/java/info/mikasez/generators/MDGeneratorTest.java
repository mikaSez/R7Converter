package info.mikasez.generators;

import info.mikasez.generators.matchers.MDTagMatcher;
import info.mikasez.models.DocType;
import info.mikasez.models.Element;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * Created by MikaSez on 27/10/2015.
 */
public class MDGeneratorTest {
    private Generator tested;


    @Before
    public void setUp() {
        Element element = new Element(DocType.Root);
        Element p = new Element(DocType.Paragraph);
        p.addTextChild("On July 2,");
        Element ocode = new Element(DocType.OneLineCode);
        ocode.addTextChild("an alien mothership");
        p.addChild(ocode);
        p.addTextChild("entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide.");
        Element h = new Element(DocType.Header1);
        h.addTextChild("Header1");
        Element h2 = new Element(DocType.Header2);

        h2.addTextChild("Header2");
        Element h3 = new Element(DocType.Header3);

        h3.addTextChild("Header3");


        element.addChild(h);
        element.addChild(h2);
        element.addChild(h3);
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

        Element bq = new Element(DocType.BlockQuote);
        bq.addTextChild("Pardon my french is a blockquote");
        Element em = new Element(DocType.Emphasis);
        Element sem = new Element(DocType.StrongEmphasis);

        em.addTextChild("Text in italic");
        sem.addTextChild("Bold Text");
        bq.addChild(em);
        bq.addChild(sem);
        element.addChild(bq);


        tested = new Generator(element, new MDTagMatcher());
    }


    @Test
    public void generateTest() {
        StringBuilder sb = new StringBuilder();
        sb.append("# Header1\n");
        sb.append("## Header2\n");
        sb.append("### Header3\n");
        sb.append("On July 2, `an alien mothership` entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide.\n");
        sb.append("* Item 1\n");
        sb.append("* Item 2\n");
        sb.append("* Item 3\n");
        sb.append("\n");
        sb.append("> Pardon my french is a blockquote *Text in italic*  **Bold Text** ");

        sb.append("\n");
        sb.append("\n");
        Assert.assertEquals(sb.toString(), tested.generate());
    }

}
