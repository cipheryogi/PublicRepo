''' re is a Python module that provides support for regular expressions. Regular expressions are a powerful way to search for and manipulate text using patterns. The re module allows you to work with regular expressions in Python, making it easy to perform tasks like searching, matching, and extracting text patterns within strings.

Here are some common functions and methods provided by the re module:

re.compile(pattern): Compiles a regular expression pattern into a regex object, which can be used for pattern matching.

re.search(pattern, string): Searches for the first occurrence of the pattern in the given string and returns a match object.

re.match(pattern, string): Checks if the pattern matches at the beginning of the string and returns a match object.

re.findall(pattern, string): Returns a list of all non-overlapping matches of the pattern in the string.

re.finditer(pattern, string): Returns an iterator yielding match objects for all matches of the pattern in the string.

re.sub(pattern, replacement, string): Replaces all occurrences of the pattern in the string with the specified replacement.

Various methods in match objects, such as group(), start(), and end(), allow you to access information about the matched text.

The re module is a standard library module in Python, so you don't need to install any external packages to use it. It's a powerful tool for working with text and performing text processing tasks that involve pattern matching. 

In this example -
The ip_pattern is a regular expression pattern used to match IPv4 addresses in a given text. Let's break down the components of this pattern:

\b: This is a word boundary anchor. It ensures that the IP address is surrounded by word boundaries, which means it matches whole IP addresses and not parts of IP addresses within words. For example, it won't match "192.168.1.1000" as part of "192.168.1.1000abc."

(?: ... ): This is a non-capturing group. It's used to group together a portion of the regular expression without capturing it as a separate group in the match result. In this case, it's used to group the pattern for matching each octet of the IP address.

\d{1,3}: This part matches one to three digits. This is used to match each octet (each part of the IP address) because each octet can have one to three digits (e.g., 192 or 10 or 8).

\.: This matches the literal period (dot) character, which separates octets in an IP address.

{3}: This specifies that the previous group (the combination of one to three digits and a period) should be repeated exactly three times, as there are three periods separating four octets in an IPv4 address.

\d{1,3}: This is used to match the last octet of the IP address.

\b: Another word boundary anchor, ensuring that the IP address ends with a word boundary.

So, the regular expression r'\b(?:\d{1,3}\.){3}\d{1,3}\b' is designed to match IPv4 addresses by looking for four octets separated by periods, where each octet can have one to three digits. The \b anchors ensure that it matches complete IP addresses within the text and not partial matches within words or numbers.
'''

import re

def extract_ip_addresses(text):
    # Define a regular expression pattern to match both IPv4 and IPv6 addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'

    # Use the findall method to extract all IP addresses from the text
    ip_addresses = re.findall(ip_pattern, text)

    return ip_addresses

# Example usage:
text_input = "Here are some example IP addresses: 192.168.1.1, 10.0.0.1, 2001:0db8:85a3:0000:0000:8a2e:0370:7334, and 8.8.8.8. Make sure to extract them! Random text"
ip_addresses = extract_ip_addresses(text_input)

if ip_addresses:
    print("IP addresses found:")
    for ip in ip_addresses:
        print(ip)
else:
    print("No IP addresses found in the text input.")


