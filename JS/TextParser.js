// Sample text input with IP addresses
const textInput =
  "Here are some IP addresses:\n" +
  "192.168.1.1\n" +
  "10.0.0.1\n" +
  "Invalid IP: 256.256.256.256\n" +
  "Another IP: 172.16.0.1";

// Regular expression pattern to match IP addresses
const ipRegex = /\b(?:\d{1,3}\.){3}\d{1,3}\b/g;

// Function to find and print IP addresses
function findIPAddresses(text) {
  const matches = text.match(ipRegex);
  if (matches) {
    for (const match of matches) {
      console.log(match);
    }
  } else {
    console.log("No IP addresses found.");
  }
}

// Call the function with the input text
findIPAddresses(textInput);
