import numpy as np

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        # If the max depth is reached or all labels are the same, return a leaf node
        if self.max_depth is not None and depth >= self.max_depth or len(np.unique(y)) == 1:
            return Node(label=self._most_common_label(y))

        # Find the best split feature and value
        best_feature, best_value = self._find_best_split(X, y)

        if best_feature is None or best_value is None:
            return Node(label=self._most_common_label(y))

        # Split the data based on the best split
        left_indices = X[best_feature] < best_value
        X_left, y_left = X[left_indices], y[left_indices]
        X_right, y_right = X[~left_indices], y[~left_indices]

        # Recursively build the left and right subtrees
        left_subtree = self._build_tree(X_left, y_left, depth + 1)
        right_subtree = self._build_tree(X_right, y_right, depth + 1)

        return Node(feature=best_feature, value=best_value, left=left_subtree, right=right_subtree)

    def _find_best_split(self, X, y):
        best_gini = 1.0
        best_feature, best_value = None, None
        n_features = X.shape[1]

        for feature in range(n_features):
            values = np.unique(X[:, feature])
            for value in values:
                left_indices = X[:, feature] < value
                gini = self._calculate_gini(y[left_indices], y[~left_indices])
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_value = value

        return best_feature, best_value

    def _calculate_gini(self, left_labels, right_labels):
        left_size, right_size = len(left_labels), len(right_labels)
        total_size = left_size + right_size

        if total_size == 0:
            return 0.0

        p_left, p_right = left_size / total_size, right_size / total_size

        gini_left = 1.0 - sum([(np.sum(left_labels == label) / left_size) ** 2 for label in np.unique(left_labels)])
        gini_right = 1.0 - sum([(np.sum(right_labels == label) / right_size) ** 2 for label in np.unique(right_labels)])

        gini = p_left * gini_left + p_right * gini_right

        return gini

    def _most_common_label(self, y):
        return np.bincount(y).argmax()

    def predict(self, X):
        return [self._predict_sample(sample) for _, sample in X.iterrows()]

    def _predict_sample(self, sample):
        node = self.tree
        while node.label is None:
            if sample[node.feature] < node.value:
                node = node.left
            else:
                node = node.right
        return node.label

class Node:
    def __init__(self, feature=None, value=None, label=None, left=None, right=None):
        self.feature = feature  # Index of feature to split on (for internal nodes)
        self.value = value      # Split value for the feature (for internal nodes)
        self.label = label      # Class label (for leaf nodes)
        self.left = left        # Left subtree
        self.right = right      # Right subtree
