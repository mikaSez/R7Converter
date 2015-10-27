package info.mikasez.processors;

import org.junit.Test;

import java.io.FileInputStream;
import java.util.Properties;

/**
 * Created by MikaSez on 11/10/2015.
 */
public class MarkdownProcessorTest {

    @Test
    public void loadPropertiesTest() throws Exception {

        Properties props = new Properties();
        props.load(new FileInputStream("./src/test/resources/fileResources/md.properties"));
        System.out.println(props);
        props.stringPropertyNames().forEach(System.out::println);
    }
}
