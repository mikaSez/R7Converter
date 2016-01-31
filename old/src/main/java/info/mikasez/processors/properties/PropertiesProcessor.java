package info.mikasez.processors.properties;

import info.mikasez.processors.FileProcessor;
import info.mikasez.processors.exception.ProcessException;

import java.util.List;

/**
 * Created by MikaSez on 08/10/2015.
 */
public class PropertiesProcessor implements FileProcessor {
    private List<Propertie> properties;

    public PropertiesProcessor(List<Propertie> props) {
        properties = props;
    }

    @Override
    public void process(String line) throws ProcessException {
    }
}
