package info.mikasez.processors;

import info.mikasez.processors.exception.ProcessException;

/**
 * Interface used by the reader to apply an action on each line of the processed document
 */
public interface FileProcessor {

    void process(String line) throws ProcessException;
}
