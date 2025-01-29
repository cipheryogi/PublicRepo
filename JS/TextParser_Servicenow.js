// Define a regular expression pattern to match IP addresses
var ipPattern = /\b(?:\d{1,3}\.){3}\d{1,3}\b/g;

// Sample text containing random text and IP addresses
var inputText = "This is a sample text with IP addresses 192.168.1.1 and 10.0.0.1 embedded within it. ajhdeuhguiebetitbiub 10.10.1.1 reiughirfebibiuce";

// Function to extract IP addresses from the input text
function extractIPAddresses(text) {
  var ipAddresses = [];
  var matches = text.match(ipPattern);
  
  if (matches) {
    ipAddresses = matches;
  }
  
  return ipAddresses;
}

// Call the function to extract IP addresses from the input text
var extractedIPs = extractIPAddresses(inputText);

// Output the discovered IP addresses
for (var i = 0; i < extractedIPs.length; i++) {
  gs.info("Discovered IP Address: " + extractedIPs[i]);
}