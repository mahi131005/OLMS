const techFacts = [
  {
    fact: "WebDev: HTTP/3 uses QUIC for faster and more secure communication.",
    explanation: "QUIC (Quick UDP Internet Connections) reduces latency and improves security by combining encryption and transport layer functionality."
  },
  {
    fact: "DataScience: Over 90% of the world's data was generated in the last two years.",
    explanation: "The exponential growth of data is driven by IoT devices, social media, and digital transformation."
  },
  {
    fact: "MobileDev: Flutter allows you to build apps for mobile, web, and desktop from a single codebase.",
    explanation: "Flutter is a UI toolkit by Google that uses the Dart programming language for cross-platform development."
  },
  {
    fact: "AIML: GPT-4 can process and generate human-like text for natural language processing.",
    explanation: "GPT-4 is a state-of-the-art language model that uses deep learning to understand and generate text."
  },
  {
    fact: "CyberSec: Multi-factor authentication (MFA) prevents 99.9% of automated attacks.",
    explanation: "MFA adds an extra layer of security by requiring multiple forms of verification, such as a password and a one-time code."
  },
  {
    fact: "CloudComputing: Serverless computing eliminates the need to manage servers.",
    explanation: "Serverless platforms like AWS Lambda automatically handle server provisioning and scaling, allowing developers to focus on code."
  },
  {
    fact: "Tech: The first computer virus, 'Creeper,' was created in 1971.",
    explanation: "Creeper was an experimental program that displayed the message, 'I'm the creeper, catch me if you can!'"
  },
  {
    fact: "WebDev: React.js uses a virtual DOM for optimized rendering.",
    explanation: "The virtual DOM allows React to update only the parts of the UI that change, improving performance."
  },
  {
    fact: "DataScience: Python's Pandas library is built on top of NumPy.",
    explanation: "Pandas provides high-level data manipulation tools, while NumPy offers efficient numerical operations."
  },
  {
    fact: "MobileDev: Swift is Apple's preferred language for iOS development.",
    explanation: "Swift is designed for performance and safety, making it easier to write reliable and efficient code."
  },
  {
    fact: "AIML: Reinforcement learning trains AI models by rewarding desired behaviors.",
    explanation: "This approach is inspired by behavioral psychology and is used in applications like game AI and robotics."
  },
  {
    fact: "CyberSec: A zero-day vulnerability is a security flaw unknown to the vendor.",
    explanation: "Attackers exploit these vulnerabilities before developers can release a patch, making them highly dangerous."
  },
  {
    fact: "CloudComputing: AWS Lambda runs code without provisioning servers.",
    explanation: "Lambda executes code in response to events and automatically scales based on demand."
  },
  {
    fact: "Tech: The first programmable computer, the Z1, was created in 1938.",
    explanation: "The Z1, designed by Konrad Zuse, was the first binary programmable computer."
  },
  {
    fact: "WebDev: CSS Grid simplifies complex layouts.",
    explanation: "CSS Grid allows developers to create responsive and flexible layouts with minimal code."
  },
  {
    fact: "DataScience: 'Big data' refers to datasets too large for traditional processing.",
    explanation: "Big data requires specialized tools like Hadoop and Spark for storage and analysis."
  },
  {
    fact: "MobileDev: Kotlin is now preferred over Java for Android development.",
    explanation: "Kotlin is more concise and safer than Java, reducing the likelihood of runtime errors."
  },
  {
    fact: "AIML: Neural networks mimic the human brain's structure.",
    explanation: "Neural networks consist of layers of interconnected nodes that process data similarly to neurons."
  },
  {
    fact: "CyberSec: Phishing attacks trick users into revealing sensitive information.",
    explanation: "Phishing often involves fake emails or websites that appear legitimate to steal data."
  },
  {
    fact: "CloudComputing: Kubernetes automates containerized application deployment.",
    explanation: "Kubernetes manages container orchestration, scaling, and load balancing."
  },
  {
    fact: "Tech: The first email was sent in 1971 by Ray Tomlinson.",
    explanation: "Tomlinson also introduced the '@' symbol to separate the user and domain names."
  },
  {
    fact: "WebDev: JavaScript is the most popular programming language.",
    explanation: "JavaScript is widely used for both front-end and back-end development, thanks to frameworks like Node.js."
  },
  {
    fact: "DataScience: Machine learning models improve with more data.",
    explanation: "Larger datasets help models generalize better and make more accurate predictions."
  },
  {
    fact: "MobileDev: Progressive Web Apps (PWAs) work offline.",
    explanation: "PWAs use service workers to cache resources, enabling offline functionality."
  },
  {
    fact: "AIML: Computer vision enables machines to interpret images.",
    explanation: "Applications include facial recognition, object detection, and medical imaging."
  },
  {
    fact: "CyberSec: Encryption protects data from unauthorized access.",
    explanation: "Encryption converts data into a secure format that can only be read with the correct key."
  },
  {
    fact: "CloudComputing: Google Cloud offers AI and machine learning tools.",
    explanation: "Tools like AutoML and TensorFlow on Google Cloud simplify AI development."
  },
  {
    fact: "Tech: The first website went live in 1991.",
    explanation: "The website, created by Tim Berners-Lee, explained the World Wide Web project."
  },
  {
    fact: "WebDev: Bootstrap simplifies responsive web design.",
    explanation: "Bootstrap provides pre-designed components and a grid system for building responsive websites."
  },
  {
    fact: "DataScience: Data visualization helps in understanding complex data.",
    explanation: "Tools like Matplotlib and Tableau create visual representations of data for easier analysis."
  },
  {
    fact: "MobileDev: Android Studio is the official IDE for Android development.",
    explanation: "Android Studio provides tools for coding, debugging, and testing Android apps."
  },
  {
    fact: "AIML: Natural Language Processing (NLP) powers chatbots.",
    explanation: "NLP enables machines to understand and respond to human language."
  },
  {
    fact: "CyberSec: Firewalls monitor and control network traffic.",
    explanation: "Firewalls act as a barrier between trusted and untrusted networks, blocking malicious traffic."
  },
  {
    fact: "CloudComputing: Microsoft Azure supports hybrid cloud environments.",
    explanation: "Azure allows businesses to integrate on-premises infrastructure with cloud services."
  },
  {
    fact: "Tech: The first smartphone was IBM's Simon, released in 1994.",
    explanation: "Simon featured a touchscreen and could send emails and faxes."
  },
  {
    fact: "WebDev: WebAssembly allows running high-performance code in browsers.",
    explanation: "WebAssembly enables near-native performance for web applications, written in languages like C++."
  },
  {
    fact: "DataScience: SQL is essential for querying databases.",
    explanation: "SQL (Structured Query Language) is used to retrieve and manipulate data in relational databases."
  },
  {
    fact: "MobileDev: React Native enables cross-platform mobile app development.",
    explanation: "React Native allows developers to write apps for iOS and Android using a single codebase."
  },
  {
    fact: "AIML: Generative Adversarial Networks (GANs) create realistic images.",
    explanation: "GANs consist of two neural networks that compete to generate and refine images."
  },
  {
    fact: "CyberSec: VPNs encrypt internet connections for privacy.",
    explanation: "VPNs (Virtual Private Networks) create a secure tunnel for data transmission over the internet."
  },
  {
    fact: "CloudComputing: Docker containers simplify application deployment.",
    explanation: "Docker packages applications and their dependencies into lightweight, portable containers."
  },
  {
    fact: "Tech: The first computer mouse was made of wood.",
    explanation: "Douglas Engelbart invented the mouse in 1964, and it had two perpendicular wheels for movement."
  },
  {
    fact: "WebDev: APIs enable communication between software applications.",
    explanation: "APIs (Application Programming Interfaces) define how different software components interact."
  },
  {
    fact: "DataScience: Overfitting occurs when a model learns noise instead of patterns.",
    explanation: "Overfitting happens when a model is too complex and performs well on training data but poorly on new data."
  },
  {
    fact: "MobileDev: Jetpack Compose simplifies UI development for Android.",
    explanation: "Jetpack Compose is a modern toolkit for building native UIs with less code."
  },
  {
    fact: "AIML: Transfer learning allows reusing pre-trained models.",
    explanation: "Transfer learning leverages knowledge from one task to improve performance on another related task."
  },
  {
    fact: "CyberSec: Ransomware encrypts files and demands payment for decryption.",
    explanation: "Ransomware attacks can cripple organizations by locking access to critical data."
  },
  {
    fact: "CloudComputing: Edge computing processes data closer to the source.",
    explanation: "Edge computing reduces latency by processing data near the device instead of in a centralized cloud."
  },
  {
    fact: "Tech: The first domain name ever registered was Symbolics.com.",
    explanation: "Symbolics.com was registered on March 15, 1985, marking the beginning of the domain name system."
  },
  {
    fact: "WebDev: GraphQL allows clients to request specific data from APIs.",
    explanation: "GraphQL provides a flexible and efficient alternative to REST APIs by letting clients define the data they need."
  },
  {
    fact: "DataScience: Feature engineering improves model accuracy.",
    explanation: "Feature engineering involves selecting and transforming variables to make them more useful for machine learning models."
  },
  {
    fact: "MobileDev: SwiftUI is Apple's declarative framework for building UIs.",
    explanation: "SwiftUI simplifies UI development by allowing developers to describe the interface declaratively."
  },
  {
    fact: "AIML: AI ethics focuses on fairness, accountability, and transparency.",
    explanation: "AI ethics ensures that AI systems are designed and used responsibly, avoiding bias and harm."
  },
  {
    fact: "CyberSec: Penetration testing identifies system vulnerabilities.",
    explanation: "Penetration testing simulates attacks to uncover weaknesses in a system's defenses."
  },
  {
    fact: "CloudComputing: Serverless functions scale automatically with demand.",
    explanation: "Serverless platforms like AWS Lambda automatically adjust resources based on the workload."
  },
  {
    fact: "Tech: The first web browser was called WorldWideWeb.",
    explanation: "WorldWideWeb, created by Tim Berners-Lee in 1990, was the first browser to display web pages."
  },
  {
    fact: "WebDev: WebSockets enable real-time communication between clients and servers.",
    explanation: "WebSockets provide a persistent connection for real-time data exchange, unlike traditional HTTP requests."
  },
  {
    fact: "DataScience: Clustering groups similar data points together.",
    explanation: "Clustering is an unsupervised learning technique used to identify patterns and group data."
  },
  {
    fact: "MobileDev: Android Jetpack provides libraries for common tasks.",
    explanation: "Jetpack simplifies Android development by offering pre-built components for navigation, database access, and more."
  },
  {
    fact: "AIML: AI can generate art, music, and even poetry.",
    explanation: "AI models like DALL-E and GPT-3 can create creative content by learning patterns from existing works."
  },
  {
    fact: "CyberSec: Biometric authentication uses fingerprints or facial recognition.",
    explanation: "Biometric authentication provides a secure and convenient way to verify identity using unique physical traits."
  }
];

// DOM Elements
const popup = document.getElementById('popup');
const techFactElement = document.getElementById('tech-fact');
const techExplanationElement = document.getElementById('tech-explanation');
const thumbsUpBtn = document.getElementById('thumbs-up');
const thumbsDownBtn = document.getElementById('thumbs-down');
const closePopupBtn = document.getElementById('close-popup');

// Function to Show Pop-up
function showPopup() {
  const randomFact = techFacts[Math.floor(Math.random() * techFacts.length)];
  techFactElement.textContent = randomFact.fact;
  techExplanationElement.textContent = randomFact.explanation;
  popup.style.display = 'flex';
  document.body.classList.add('blur-background');

  // Mark the popup as shown in localStorage
  localStorage.setItem('popupShown', 'true');
}

// Function to Close Pop-up
function closePopup() {
  popup.style.display = 'none';
  document.body.classList.remove('blur-background');
}

// Function to Clear Popup Flag (Call this on logout)
function clearPopupFlag() {
  localStorage.removeItem('popupShown');
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
  // Check if the popup has already been shown in this session
  const popupShown = localStorage.getItem('popupShown');

  // Show popup only if it hasn't been shown in this session
  if (!popupShown) {
    setTimeout(showPopup, 2000); // Simulate post-login delay
  }
});

closePopupBtn.addEventListener('click', closePopup);

// Thumbs Up/Down Functionality
thumbsUpBtn.addEventListener('click', () => {
  thumbsUpBtn.classList.add('active');
  thumbsDownBtn.classList.remove('active');
});

thumbsDownBtn.addEventListener('click', () => {
  thumbsDownBtn.classList.add('active');
  thumbsUpBtn.classList.remove('active');
});