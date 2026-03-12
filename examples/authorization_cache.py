from linqex import Enumerable
from dataclasses import dataclass

@dataclass
class UserContext:
    user_id: int
    role: str
    is_active: bool

class AuthorizationCache:
    """
    Builds a high-performance, read-only index of users based on their roles.
    Demonstrates the power of `to_lookup` over a standard dictionary.
    """
    
    def __init__(self, all_users: list[UserContext]):
        # Instead of manually writing loops with defaultdict, 
        # we let PyLINQ build an indexed lookup table in one line.
        
        self._role_index = (Enumerable(all_users)
            # Only index active users
            .where(lambda u: u.is_active)
            # Group them by 'role', and store the 'user_id'
            .to_lookup(
                key_selector=lambda u: u.role,
                element_selector=lambda u: u.user_id
            ))

    def get_active_user_ids_by_role(self, role: str) -> list[int]:
        """
        Fetches users for a given role. 
        If the role doesn't exist (e.g., 'SuperAdmin'), a standard Dict would throw a KeyError.
        The Lookup gracefully returns an empty Enumerable.
        """
        # Fast Path lookup (O(1)). Returns an Enumerable, so we cast to list.
        # Notice we don't need a try/except or .get() block!
        users_in_role = self._role_index.get(role, Enumerable())
        
        return users_in_role.to_list()

if __name__ == "__main__":
    db_users = [
        UserContext(1, "Admin", True),
        UserContext(2, "Editor", True),
        UserContext(3, "Admin", False), # Inactive
        UserContext(4, "Viewer", True),
        UserContext(5, "Editor", True)
    ]

    auth_cache = AuthorizationCache(db_users)

    print("Active Admins:", auth_cache.get_active_user_ids_by_role("Admin"))
    print("Active Editors:", auth_cache.get_active_user_ids_by_role("Editor"))
    
    # Requesting a role that has no active users (or doesn't exist)
    # This proves why `to_lookup` is safer and cleaner than `to_dict`
    print("Active SuperAdmins:", auth_cache.get_active_user_ids_by_role("SuperAdmin"))
