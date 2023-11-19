# HacksArena - Event App

HacksArena is an event management application designed to streamline the organization and participation in hackathons. Whether you are hosting a hackathon or looking to participate, HacksArena provides a centralized platform to manage events, connect with participants, and stay updated on upcoming hackathons.

## Features

- **User Registration and Authentication:**
  - Users can create accounts on HacksArena.
  - Social account login support for GitHub and Google.
  - Password setting for users who sign up with social accounts.

- **Event Management:**
  - Hosts can create and manage hackathon events.
  - Participants can explore and register for upcoming hackathons.

- **Event Details:**
  - Detailed information about each hackathon, including date, time, location, and description.

- **User Profiles:**
  - Participants can create profiles showcasing their skills and interests.
  - Search functionality to find and connect with other users.

- **Search Functionality:**
  - Search for hackathons based on titles and descriptions.
  - Search for users based on usernames and names.

## Getting Started

### Prerequisites

- Python (version 3.11.5 recommended)
- Django (version 4.1.13 recommended)
- Djongo (for MongoDB integration)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hk669/HacksArena.git
   cd HackArena
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

```bash

export SECRET_KEY="your-secret-key"
export CLIENT_ID="client-id"
export SECRET_GITHUB="client-secret"

```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

1. **User Registration:**
   - Create an account on HacksArena.
   - Use social accounts (GitHub, Google) for quick registration.

2. **Explore Events:**
   - Browse upcoming hackathons.
   - View detailed information about each event.

3. **Event Registration:**
   - Register for hackathons you're interested in.

4. **User Profiles:**
   - Create and customize your user profile.
   - Connect with other participants.

5. **Search Functionality:**
   - Use the search feature to find hackathons or users.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project uses the Django web framework and Djongo for MongoDB integration.
- The project can be used both on sql and also mongoDB.

---
