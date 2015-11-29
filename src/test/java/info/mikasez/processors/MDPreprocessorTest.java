package info.mikasez.processors;

import info.mikasez.processors.properties.Line;
import info.mikasez.processors.properties.MDPreprocessor;
import org.junit.Assert;
import org.junit.Test;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by MikaSez on 15/10/2015.
 */
public class MDPreprocessorTest {

    MDPreprocessor tested = new MDPreprocessor();

    @Test
    public void processTest() throws FileNotFoundException {
        FileInputStream stream = new FileInputStream("./src/test/resources/fileResources/preProcessorTest");
        Queue<Line> queue = new LinkedList<Line>() {{
            add(new Line(true, "The content of this file is taken directly from markdown documentation for test purposes"));
            add(new Line(true, ""));
            add(new Line(true, "On July 2, an alien mothership entered Earth's orbit and deployed several dozen saucer-shaped \"destroyer\" spacecraft, each 15 miles (24 km)  wide."));
            add(new Line(true, ""));
            add(new Line(false, "# The largest heading (an <h1> tag)"));
            add(new Line(false, "* Item"));
            add(new Line(false, "* Item"));
            add(new Line(true, "*This text will be italic*"));
            add(new Line(true, "**This text will be bold**"));

            add(new Line(false, "```ruby"));
            add(new Line(true, "require 'redcarpet'"));
            add(new Line(true, "markdown = Redcarpet.new(\"Hello World!\")"));
            add(new Line(true, "puts markdown.to_html"));
            add(new Line(false, "```"));

        }};
        tested.process(stream);

        Queue<Line> lines = tested.getProcessed();

        Assert.assertEquals(queue, lines);
    }
}
