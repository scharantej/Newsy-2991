## App Design for Displaying Recent News Articles

### HTML Files

- **index.html**: This is the main page of the application. It will contain the necessary structure and elements to display the recent news articles.
  - The HTML should include elements like a header, navigation bar, and a main section where the news articles will be displayed.

### Routes

- **`/`**: This route will handle requests to the main page of the application.
  - It should render the `index.html` file.

- **`/news_articles`**: This route will handle requests to fetch recent news articles.
  - It should make an API call to a news API to retrieve the latest news articles.
  - The response from the API call should be processed and the extracted news articles should be stored in a database.
  - The stored news articles should be returned as a JSON response to the client.