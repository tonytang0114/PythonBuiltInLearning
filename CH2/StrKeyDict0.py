class StrKeyDict0(dict): # inherit from dictionary
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

# StrKeyDict0 inherits from dict
# Check whether key is already a str. If it is, and it's missing, raise KeyError.
# Build str from key and look it up
# The get method delegates to __getitem__ by using self[key] notation; that gives the opportunity for our __missing__ to act.
# If a KeyError is raised, __missing__ already failed, so we return the result
# Search for unmodified key (the instance may contain non-str keys), then for a str built from the key.
# The method inherited from dict does not fall back to invoking __missing__.
