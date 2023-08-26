from bs4 import BeautifulSoup
import pytest
from scrapper import (
    get_soup,
    get_image_links,
    get_username,
    get_generation_params,
    get_model_used,
    get_prompt_used
)

@pytest.fixture
def sample_soup():
    html = """
    <div class="mt-1 text-left card py-3 px-4">
        Sample Generation Params
    </div>
    <div class="d-inline-flex align-items-center" style="">

      <a style="color: inherit; text-decoration-color: rgba(0, 0, 0, 0.1); font-weight: 500;" data-turbo-frame="_top" href="https://prompthero.com/DameVee">
        <span class="">DameVee
</span></a>

    </div>
    <div class="mt-1 text-center card py-3 px-4">
            
<a class="d-inline" style="color: inherit; border-color: inherit;" href="/openjourney--4-prompts">
  <span class="">
    <i class="fa-solid fa-robot"></i>
    Openjourney
    <span class="small text-muted" style="text-transform: uppercase; font-size: 12px; vertical-align: middle;">4</span>
  </span>
</a>


        </div>
        
        <div class="col-12 col-md-7 text-center">

        <img src="https://prompthero.com/rails/active_storage/representations/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1WWpsaU1EZzJOUzFoWXpOaUxUUTBOVFV0WVRjd09TMHdaamRrWkRnNE9USTNOVEFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--18dfa410bf5eba28848fc4caddceef82a29c5fe0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBPZ2wzWldKd09oUnlaWE5wZW1WZmRHOWZiR2x0YVhSYkIya0NBQWd3T2dwellYWmxjbnNKT2hOemRXSnpZVzF3YkdWZmJXOWtaVWtpQjI5dUJqb0dSVlE2Q25OMGNtbHdWRG9PYVc1MFpYSnNZV05sVkRvTWNYVmhiR2wwZVdsZiIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--935666d13f63ed5aca9daa2416340e3a90b6014e/prompthero-prompt-4ae9caa7ad7.png" class="img-fluid" style="border-radius: 4px;">

        <p class="small mt-3" style="opacity: 0.6;">
            Want to learn how to create images like this one?
          <br> Check out our <a style="color: inherit; text-decoration: underline;" href="/academy/prompt-engineering-course">crash course in prompt engineering &amp; AI art generation</a>!
        </p>

        <div class="mt-5 text-left">
          <div class="small text-muted">
  <div class="small text-muted my-2">
      <a style="color: inherit; text-decoration-color: rgba(0, 0, 0, 0.1); font-weight: 500;" href="https://prompthero.com/DameVee">
        <span class="">DameVee
</span></a>    posted about 1 month ago
  </div>

  <div>
    <span class="mr-2"><i class="fa-solid fa-eye"></i> 120 views</span>

    <span class="mr-2"><i class="fa-solid fa-comments"></i> 0 comments</span>
  </div>
</div>


        </div>

        <div class="my-4 text-center">
          <a target="_blank" class="btn btn-sm btn-outline-action" href="https://twitter.com/intent/tweet?text=Check+out+this+Openjourney+prompt+on+%40PromptHero%21+https%3A%2F%2Fprompthero.com%2Fprompt%2F4ae9caa7ad7">
            <i class="fa-brands fa-twitter"></i> Share this prompt on Twitter
</a>        </div>

        <div class="mt-4 text-left">
          <turbo-frame loading="lazy" id="comments" src="https://prompthero.com/prompt/4ae9caa7ad7/comments">


  <h3 class="stylish-header">Comments (<span id="prompt-comments-count">0</span>)</h3>


    <div class="text-center card py-5 px-4 mt-4">
    <p class="d-inline my-0">
      <a data-turbo-frame="_top" style="color: inherit; text-decoration: underline; text-decoration-color: rgba(0, 0, 0, 0.35); font-weight: bolder;" href="/users/sign_up">👉 Join the community</a> to comment. Already a prompter? <a data-turbo-frame="_top" style="color: inherit; text-decoration: underline; text-decoration-color: rgba(0, 0, 0, 0.35); font-weight: bolder;" href="/users/sign_in">Log in</a>
    </p>
  </div>


  <div class="container my-5">
  <div class="row">
    <div class="col-12 col-md-6 offset-md-3 text-center">
      
    </div>
  </div>
</div>

  <div id="comments-history"></div>
</turbo-frame>        </div>

      </div>
    """
    return BeautifulSoup(html, 'html.parser')

def test_get_image_links(sample_soup):
    image_links = get_image_links(sample_soup)
    assert image_links == ["https://prompthero.com/rails/active_storage/representations/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1WWpsaU1EZzJOUzFoWXpOaUxUUTBOVFV0WVRjd09TMHdaamRrWkRnNE9USTNOVEFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--18dfa410bf5eba28848fc4caddceef82a29c5fe0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBPZ2wzWldKd09oUnlaWE5wZW1WZmRHOWZiR2x0YVhSYkIya0NBQWd3T2dwellYWmxjbnNKT2hOemRXSnpZVzF3YkdWZmJXOWtaVWtpQjI5dUJqb0dSVlE2Q25OMGNtbHdWRG9PYVc1MFpYSnNZV05sVkRvTWNYVmhiR2wwZVdsZiIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--935666d13f63ed5aca9daa2416340e3a90b6014e/prompthero-prompt-4ae9caa7ad7.png"]

def test_get_username(sample_soup):
    username = get_username(sample_soup)
    assert username == "DameVee"

def test_get_generation_params(sample_soup):
    generation_params = get_generation_params(sample_soup)
    assert generation_params == "Sample Generation Params"

def test_get_model_used(sample_soup):
    model_used = get_model_used(sample_soup)
    assert model_used == "Openjourney\n    4"
    
def test_get_prompt_used(sample_soup):
    model_used = get_prompt_used(sample_soup)
    assert model_used == "crash course in prompt engineering & AI art generation"

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main()
