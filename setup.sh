mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"202018007@daiict.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml