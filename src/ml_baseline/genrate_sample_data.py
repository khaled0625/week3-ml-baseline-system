# import pandas as pd
# import numpy as np
# from pathlib import Path
#
# # # Setup Path
# data_dir = Path("data/processed")
# data_dir.mkdir(parents=True, exist_ok=True)
# #
#
#
# def make_sample_data(*, root: Path | None = None, n_users: int = 50, seed: int = 100):
#     paths = Paths.from_repo_root() if root is None else Paths(root=root)
#     paths.data_processed_dir.mkdir(parents=True, exist_ok=True)
#
#     rng = np.random.default_rng(seed)
#     user_id = [f"u{i:03d}" for i in range(1, n_users + 1)]
#     country = rng.choice(["SA","KW", "QA"], size=n_users, replace=True)
#     n_order = rng.integers(1, 10, size=n_users)
#     avg_amount = rng.normal(loc=10, scale=3, size=n_users).clip(min=1)
#     total_amount = n_order * avg_amount
#
#     is_high_value = (total_amount >= 80).astype(int)
#
#     df = pd.DataFrame({
#         "user_id": user_id,
#         "country": country,
#         "n_order": n_order,
#         "avg_amount": avg_amount,
#         "total_amount": total_amount,
#         "is_high_value": is_high_value,
#     })
#
#     df.to_csv(data_dir / "sample_data.csv", index=False)

import pandas as pd
import numpy as np
from pathlib import Path

# Setup Path
data_dir = Path("../../data/processed")
data_dir.mkdir(parents=True, exist_ok=True)


def make_sample_data(*, root: Path | None = None, n_users: int = 50, seed: int = 42):
    # Using the root parameter to create paths, but for this case, data_dir is sufficient
    if root is not None:
        data_dir = Path(root) / "data" / "processed"
        data_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed)
    user_id = [f"u{i:03d}" for i in range(1, n_users + 1)]
    country = rng.choice(["SA", "KW", "QA"], size=n_users, replace=True)
    n_order = rng.integers(1, 10, size=n_users)
    avg_amount = rng.normal(loc=10, scale=3, size=n_users).clip(min=1)
    total_amount = n_order * avg_amount

    # Create a binary indicator for high-value customers
    is_high_value = (total_amount >= 80).astype(int)

    # Create DataFrame
    df = pd.DataFrame({
        "user_id": user_id,
        "country": country,
        "n_order": n_order,
        "avg_amount": avg_amount,
        "total_amount": total_amount,
        "is_high_value": is_high_value,
    })

    # Save to CSV
    df.to_csv(data_dir / "sample_data.csv", index=False)




def test_import1():
    print("test import pkg")

# if __name__ == "__main__":
#     make_sample_data(root=data_dir,n_users=50, seed=42)