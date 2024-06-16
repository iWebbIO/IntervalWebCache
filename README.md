## IWC - Interval Web Cache (for [AutoRAY](https://github.com/iWebbIO/AUTORAY))

**IWC** (Interval Web Cache) is a Python Flask application designed to cache v2Ray subscriptions and HTTP responses at specified intervals. It offers a convenient way to store and retrieve frequently accessed data, improving performance and reducing unnecessary requests.

**Features:**

* Fetches v2Ray subscriptions or arbitrary URLs periodically.
* Stores the fetched data in a global variable for caching.
* Provides a Flask route (`/`) to retrieve the cached data.
* Handles situations where no data is available yet.

**Benefits:**

* **Improved Performance:** Reduces the need for frequent v2Ray subscription updates or HTTP requests, leading to faster access.
* **Centralized Caching:** Provides a central location to access cached data for v2ray clients or other applications.
* **Reduced Network Traffic:** By utilizing cached data, IWC minimizes unnecessary network requests.

**Requirements:**

* Python 3.x
* Flask
* Requests

**Installation:**

1. Clone this repository or download the files.
2. Install the required packages:

   ```bash
   pip install flask requests
   ```

**Usage:**

1. Configure the following variables at the top of the `IWC.py` file:

   * `URL`: The URL of your v2Ray subscription or the HTTP resource you want to cache.
   * `UPDATE_INTERVAL`: The time interval (in seconds) between updates (e.g., `5 * 60` for 5 minutes).

2. Run the program:

   ```bash
   python app.py
   ```

3. Access the cached data using a browser or v2ray client by entering `http://host:port/`
