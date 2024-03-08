https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACGKM1AG2LK5oBGWbN14soAZxbcyAHQh0GzFhACu9bOKkRU8gGaNiMFhIAWNCNgxwAHqkZwJUxU1aqaeFhdSqynhxAAJnCM8vLuWFAA5nAA+sSoZBIAFGQ0fHAAvLJgAIKMZiwA0lBBxFxQLLnoOZ56NFwVAlxZACqMqnAAlGEQAO7ppiwREjTBAlCMyV2I8izzwzQY3r6xEvzBUzkScC2EFIGxajACIfF6sQIWErUsOQBy6qeMLMR6LABC17cADJ4AjD8-iwAEw-HoQADEuRMZEYFiiXkCLGS212cH2cEOx2e50u3zAXRYZFMHGGCgAjp0uJoxpQ0vVHMTzM4dL4WAA3KBcToYO5QmESOEIlhNXYouAYKIYTwPJ4hV7vL4QG6E4nEFinFiBGgSbhQbBY8Q8CBRUbBZlwEwbEIYeTQiBechwGIvBz2Rz0kUkq0wCx0dQqeUvN6a64SqUyljgu0Cx0WCiuljuhw7cje0y+qA2APGHEK0NXFUR6UAoFdWMOp2JhUpz3p02Wp3pGjcznczqKpvrOkvZKS0ugmO9AACAU2WB4ZGS3LI2TyLBZZGIUUYsByEOC7yXK7XMGms0dCx0GDXZRgGB2WOSAGYIQt+Q+bCxMixAT8WABqN8AVhYACoVEwM9AiMU9SkCCBkgAFhvAB2e8FjmBYZAwJdkhsTwVjIS90UxbFgzxIsUi6TxghVdJsEydpOk8EgeEYTIAHJUAsABrJjEPmeQwAAXwAXSAA

import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title= "Arsh Kandola App", fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of bins", 0,100,20)

@render.plot(alt= "a histogram")
def histogram ():
  np.random.seed(3)
  x= 100+15 * np.random.rand(437)
  plt.hist(x, input,selected_number_of_bins(), density=True, color = 'pink')











def histogram
