from typing import List, Any, Optional

def count_valid_emails(emails: Optional[List[Any]]) -> int:
    """
    Count the number of valid email addresses in a list.
    
    Args:
        emails: A list of strings (or other types) to validate as email addresses.
               Can be None or non-iterable, in which case returns 0.
    
    Returns:
        int: The number of valid email addresses found. Returns 0 if input is None,
             non-iterable, empty, or contains no valid emails.
    
    Notes:
        - Validates email format: exactly one "@", non-empty local and domain parts,
          domain must contain at least one dot, no spaces allowed
        - Trims leading/trailing whitespace before validation
        - Safely handles None values, non-string types, and invalid input
        - Invalid entries (None, non-strings, malformed emails) are skipped
    """
    if emails is None:
        return 0
    
    try:
        iter(emails)
    except TypeError:
        return 0
    
    count = 0

    for email in emails:
        if is_valid_email(email):
            count += 1

    return count

def is_valid_email(email: Any) -> bool:
    """
    Check if an email address has a basic valid format.
    
    Args:
        email: A value to check (string, None, or other types).
    
    Returns:
        bool: True if email is a valid format, False otherwise.
    
    Notes:
        - Returns False for None, non-string types, or empty strings
        - Trims whitespace before validation
        - Validates: exactly one "@", non-empty local/domain parts,
          domain contains at least one dot, no spaces
    """
    # Check if email is a string and not empty (handles None and non-string types like integers, lists, dicts)
    if not isinstance(email, str) or not email:
        return False
    
    # Trim leading and trailing whitespace
    email = email.strip()
    
    # Check if email is empty after trimming
    if not email:
        return False
    
    # Must contain exactly one "@"
    if email.count("@") != 1:
        return False
    
    # Split into local and domain parts
    parts = email.split("@")
    local_part = parts[0]
    domain_part = parts[1]
    
    # Local part must not be empty
    if not local_part:
        return False
    
    # Domain part must not be empty and must contain at least one dot
    if not domain_part or "." not in domain_part:
        return False
    
    # No spaces allowed in email
    if " " in email:
        return False
    
    return True