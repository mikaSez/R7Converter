package info.mikasez.processors.exception;

/**
 * Used for errors on line processing
 */
public class ProcessException extends Exception {
    public ProcessException(String message) {
        super("Error while processing given attribut : " + message);
    }
}
