package info.mikasez.interpreters;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.AbstractMap;
import java.util.Map;

public class CommandLineInterpreterTest {

    private static final String targetFile = "/Users/MikaSez/IdeasProjects/R7Converter/src/test/resources/fileResources/targetFile";
    private static final String sourceFile = "/Users/MikaSez/IdeasProjects/R7Converter/src/test/resources/fileResources/sourceFile";
    private static final AbstractMap.SimpleEntry<String, String> result = new AbstractMap.SimpleEntry<>(sourceFile, targetFile);
    private final CommandLineInterpreter tested = new CommandLineInterpreter();

    @Before
    public void setUp() throws Exception {
        tested.commands.clear();
        tested.source = null;
        tested.target = null;
    }

    @After
    public void tearDown() throws Exception {
        Files.deleteIfExists(Paths.get(targetFile));
    }


    @Test
    public void testAddSpring() throws Exception {
        tested.add("--spring-options-and-blabla=true");

        Assert.assertEquals(tested.commands.size(), 0);
    }

    @Test
    public void testAdd() throws Exception {
        tested.add("-t");
        tested.add("/some/target/place");
        tested.add("/some/other/place");

        Assert.assertEquals(tested.commands.size(), 3);
    }


    @Test(expected = IllegalArgumentException.class)
    public void testProcessNotEnoughOptions() throws Exception {
        tested.process();
    }


    @Test(expected = IllegalArgumentException.class)
    public void testProcessTooManyOptions() throws Exception {

        tested.add("-t");
        tested.add("/some/target/place");
        tested.add("/some/other/place");

        tested.add("-t");
        tested.add("/some/target/place");
        tested.add("/some/other/place");

        tested.process();
    }


    @Test(expected = IllegalArgumentException.class)
    public void testProcessNotExistingSource() throws Exception {
        tested.add("-f");
        tested.add(targetFile);
        tested.add(targetFile);

        tested.process();
    }


    @Test(expected = IllegalArgumentException.class)
    public void testProcessExistingTarget() throws Exception {
        tested.add("-f");
        tested.add(sourceFile);
        tested.add(sourceFile);

        tested.process();
    }


    @Test
    public void testProcess3From() throws Exception {
        tested.add("-f");
        tested.add(sourceFile);
        tested.add(targetFile);

        Map.Entry<String, String> processed = tested.process();

        Assert.assertEquals(result, processed);
    }

    @Test
    public void testProcess3To() throws Exception {
        tested.add("-t");
        tested.add(targetFile);
        tested.add(sourceFile);

        Map.Entry<String, String> processed = tested.process();

        Assert.assertEquals(result, processed);
    }

    @Test
    public void testProcess2() throws Exception {
        tested.add(sourceFile);
        tested.add(targetFile);

        Map.Entry<String, String> processed = tested.process();

        Assert.assertEquals(result, processed);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testProcess2WrongOrder() throws Exception {
        tested.add(targetFile);
        tested.add(sourceFile);
        tested.process();
    }
}