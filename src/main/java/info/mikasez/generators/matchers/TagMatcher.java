package info.mikasez.generators.matchers;

import info.mikasez.models.DocType;

/**
 * Created by MikaSez on 23/11/2015.
 */
public interface TagMatcher {
    String getPostTag(DocType type);

    String getPreTag(DocType type);
}
