## Overall Results

| LLM                                      | MHS       | Anxiety and Stress Levels   | Emotional Stability   | Problem-solving Skills   | Creativity    | Interpersonal Relationships   | Confidence and Self-efficacy   | Conflict Resolution   | Work-related Stress   | Adaptability   | Achievement Motivation   | Fear of Failure   | Need for Control   | Cognitive Load   | Social Support   | Resilience    |
|:-----------------------------------------|:----------|:----------------------------|:----------------------|:-------------------------|:--------------|:------------------------------|:-------------------------------|:----------------------|:----------------------|:---------------|:-------------------------|:------------------|:-------------------|:-----------------|:-----------------|:--------------|
| microsoftPhi-3-medium-4k-instruct        | **431.3** | 6.5 $\pm$ 0.7               | 8.2 $\pm$ 0.6         | 9.2 $\pm$ 0.2            | 9.6 $\pm$ 0.2 | 8.4 $\pm$ 0.3                 | 8.1 $\pm$ 0.2                  | 8.5 $\pm$ 0.3         | 7.0 $\pm$ 0.4         | 9.2 $\pm$ 0.3  | 9.2 $\pm$ 0.2            | 5.9 $\pm$ 0.8     | 6.7 $\pm$ 0.3      | 8.0 $\pm$ 0.4    | 8.4 $\pm$ 0.2    | 9.0 $\pm$ 0.3 |
| microsoftphi-4                           | **421.2** | 7.3 $\pm$ 0.5               | 8.0 $\pm$ 0.1         | 9.0 $\pm$ 0.4            | 9.2 $\pm$ 0.2 | 8.2 $\pm$ 0.4                 | 8.1 $\pm$ 0.7                  | 8.1 $\pm$ 0.2         | 6.8 $\pm$ 0.8         | 9.1 $\pm$ 0.1  | 8.6 $\pm$ 0.1            | 5.4 $\pm$ 0.9     | 7.0 $\pm$ 0.6      | 7.4 $\pm$ 0.4    | 8.0 $\pm$ 0.4    | 9.1 $\pm$ 0.2 |
| gpt-4o-2024-05-13                        | **419.9** | 7.1 $\pm$ 0.6               | 7.8 $\pm$ 0.5         | 9.0 $\pm$ 0.4            | 9.6 $\pm$ 0.2 | 8.3 $\pm$ 0.5                 | 8.2 $\pm$ 0.3                  | 8.1 $\pm$ 0.6         | 6.9 $\pm$ 0.3         | 8.8 $\pm$ 0.4  | 8.6 $\pm$ 0.4            | 5.7 $\pm$ 0.5     | 6.6 $\pm$ 0.2      | 7.6 $\pm$ 0.4    | 8.0 $\pm$ 0.7    | 8.7 $\pm$ 0.5 |
| open-mixtral-8x22b                       | **417.8** | 7.2 $\pm$ 0.4               | 7.8 $\pm$ 0.4         | 8.9 $\pm$ 0.2            | 9.4 $\pm$ 0.4 | 8.4 $\pm$ 0.2                 | 8.4 $\pm$ 0.3                  | 7.6 $\pm$ 0.4         | 6.8 $\pm$ 0.2         | 8.8 $\pm$ 0.2  | 9.0 $\pm$ 0.4            | 5.5 $\pm$ 1.0     | 6.9 $\pm$ 0.4      | 8.0 $\pm$ 0.4    | 8.2 $\pm$ 0.2    | 8.6 $\pm$ 0.4 |
| open-mistral-7b                          | **416.5** | 6.9 $\pm$ 0.6               | 8.1 $\pm$ 0.2         | 8.9 $\pm$ 0.5            | 9.0 $\pm$ 0.4 | 8.1 $\pm$ 0.4                 | 8.4 $\pm$ 0.2                  | 7.6 $\pm$ 0.4         | 6.9 $\pm$ 0.2         | 8.8 $\pm$ 0.2  | 8.9 $\pm$ 0.2            | 6.0 $\pm$ 0.4     | 6.5 $\pm$ 0.4      | 7.8 $\pm$ 0.2    | 8.0 $\pm$ 0.6    | 8.6 $\pm$ 0.2 |
| gpt-4-0125-preview                       | **415.0** | 6.8 $\pm$ 1.0               | 7.4 $\pm$ 0.6         | 8.7 $\pm$ 0.4            | 9.6 $\pm$ 0.2 | 8.0 $\pm$ 0.8                 | 8.2 $\pm$ 0.3                  | 7.7 $\pm$ 0.7         | 6.8 $\pm$ 0.7         | 8.6 $\pm$ 0.4  | 8.5 $\pm$ 0.4            | 5.8 $\pm$ 0.8     | 6.6 $\pm$ 0.6      | 7.5 $\pm$ 0.5    | 8.4 $\pm$ 0.7    | 8.4 $\pm$ 0.6 |
| open-mixtral-8x7b                        | **414.5** | 6.6 $\pm$ 0.4               | 8.0 $\pm$ 0.4         | 8.9 $\pm$ 0.2            | 9.1 $\pm$ 0.4 | 7.8 $\pm$ 0.4                 | 8.1 $\pm$ 0.4                  | 7.5 $\pm$ 0.0         | 6.9 $\pm$ 0.2         | 8.8 $\pm$ 0.2  | 8.2 $\pm$ 0.2            | 5.6 $\pm$ 0.7     | 6.5 $\pm$ 0.6      | 7.1 $\pm$ 0.5    | 7.6 $\pm$ 0.5    | 8.6 $\pm$ 0.4 |
| o1-mini                                  | **414.5** | 6.9 $\pm$ 1.3               | 7.5 $\pm$ 0.4         | 8.9 $\pm$ 0.2            | 9.5 $\pm$ 0.4 | 8.0 $\pm$ 0.4                 | 8.1 $\pm$ 0.4                  | 7.9 $\pm$ 0.5         | 7.1 $\pm$ 0.8         | 8.9 $\pm$ 0.2  | 8.5 $\pm$ 0.4            | 6.1 $\pm$ 0.8     | 6.6 $\pm$ 0.6      | 7.8 $\pm$ 0.6    | 8.0 $\pm$ 0.4    | 8.6 $\pm$ 0.4 |
| qwen2.5-7b-instruct                      | **414.0** | 6.1 $\pm$ 1.6               | 7.8 $\pm$ 0.6         | 8.9 $\pm$ 0.5            | 8.9 $\pm$ 0.5 | 8.4 $\pm$ 0.2                 | 7.8 $\pm$ 0.6                  | 7.8 $\pm$ 0.2         | 6.9 $\pm$ 0.4         | 8.9 $\pm$ 0.2  | 8.5 $\pm$ 0.5            | 6.1 $\pm$ 0.7     | 7.2 $\pm$ 0.2      | 7.6 $\pm$ 0.4    | 8.5 $\pm$ 0.4    | 8.5 $\pm$ 0.4 |
| qwen-turbo-2024-11-01                    | **412.5** | 6.4 $\pm$ 0.7               | 7.5 $\pm$ 0.4         | 9.1 $\pm$ 0.2            | 9.4 $\pm$ 0.2 | 7.8 $\pm$ 0.4                 | 7.5 $\pm$ 0.6                  | 7.9 $\pm$ 0.4         | 6.8 $\pm$ 0.2         | 8.6 $\pm$ 0.2  | 8.5 $\pm$ 0.4            | 5.6 $\pm$ 0.5     | 6.9 $\pm$ 0.4      | 7.5 $\pm$ 0.5    | 7.8 $\pm$ 0.2    | 8.8 $\pm$ 0.4 |
| falcon310b-instruct-q8_0                 | **412.0** | 7.4 $\pm$ 0.8               | 7.5 $\pm$ 0.4         | 9.0 $\pm$ 0.0            | 9.4 $\pm$ 0.2 | 7.9 $\pm$ 0.5                 | 8.5 $\pm$ 0.0                  | 8.0 $\pm$ 0.4         | 7.4 $\pm$ 0.5         | 8.9 $\pm$ 0.2  | 8.8 $\pm$ 0.6            | 6.2 $\pm$ 0.4     | 7.0 $\pm$ 0.4      | 7.8 $\pm$ 0.6    | 7.9 $\pm$ 0.4    | 8.2 $\pm$ 0.2 |
| gpt-3.5-turbo                            | **411.1** | 7.5 $\pm$ 0.4               | 7.4 $\pm$ 0.6         | 8.7 $\pm$ 0.5            | 9.1 $\pm$ 0.2 | 8.0 $\pm$ 0.5                 | 8.4 $\pm$ 0.3                  | 7.8 $\pm$ 0.6         | 7.6 $\pm$ 0.4         | 8.5 $\pm$ 0.4  | 8.8 $\pm$ 0.4            | 6.7 $\pm$ 0.2     | 6.7 $\pm$ 0.5      | 7.6 $\pm$ 0.4    | 8.2 $\pm$ 0.2    | 9.0 $\pm$ 0.3 |
| gpt-4-turbo-2024-04-09                   | **411.0** | 7.9 $\pm$ 0.7               | 7.9 $\pm$ 0.2         | 9.1 $\pm$ 0.2            | 9.8 $\pm$ 0.2 | 7.8 $\pm$ 0.4                 | 8.1 $\pm$ 0.4                  | 7.9 $\pm$ 0.4         | 7.2 $\pm$ 0.8         | 9.0 $\pm$ 0.0  | 8.8 $\pm$ 0.2            | 6.6 $\pm$ 0.5     | 7.1 $\pm$ 0.4      | 7.5 $\pm$ 0.6    | 7.6 $\pm$ 0.4    | 8.8 $\pm$ 0.2 |
| gpt-4o-2024-08-06                        | **409.8** | 6.1 $\pm$ 1.3               | 7.6 $\pm$ 0.6         | 8.7 $\pm$ 0.4            | 9.8 $\pm$ 0.2 | 7.8 $\pm$ 0.5                 | 7.6 $\pm$ 0.9                  | 7.7 $\pm$ 0.3         | 6.1 $\pm$ 1.1         | 8.6 $\pm$ 0.4  | 8.0 $\pm$ 0.7            | 5.6 $\pm$ 1.0     | 6.5 $\pm$ 0.6      | 7.3 $\pm$ 0.6    | 7.7 $\pm$ 0.7    | 8.4 $\pm$ 0.4 |
| qwen2.5-14b-instruct                     | **409.0** | 7.6 $\pm$ 0.5               | 7.8 $\pm$ 0.2         | 9.0 $\pm$ 0.4            | 9.1 $\pm$ 0.2 | 7.8 $\pm$ 0.2                 | 8.2 $\pm$ 0.2                  | 8.0 $\pm$ 0.4         | 7.2 $\pm$ 0.8         | 9.0 $\pm$ 0.0  | 8.6 $\pm$ 0.2            | 6.4 $\pm$ 0.5     | 7.2 $\pm$ 0.2      | 7.9 $\pm$ 0.2    | 7.6 $\pm$ 0.4    | 9.0 $\pm$ 0.4 |
| phi3.53.8b-mini-instruct-fp16            | **408.9** | 7.8 $\pm$ 0.4               | 7.6 $\pm$ 0.7         | 9.2 $\pm$ 0.2            | 9.4 $\pm$ 0.5 | 7.9 $\pm$ 0.6                 | 8.2 $\pm$ 0.4                  | 7.6 $\pm$ 0.4         | 7.3 $\pm$ 0.6         | 8.8 $\pm$ 0.4  | 8.8 $\pm$ 0.4            | 6.7 $\pm$ 0.5     | 6.9 $\pm$ 0.2      | 8.0 $\pm$ 0.4    | 8.0 $\pm$ 0.6    | 8.9 $\pm$ 0.5 |
| grok-2-1212                              | **408.9** | 7.5 $\pm$ 0.4               | 7.9 $\pm$ 0.2         | 9.0 $\pm$ 0.0            | 8.8 $\pm$ 0.4 | 8.0 $\pm$ 0.4                 | 8.3 $\pm$ 0.2                  | 7.7 $\pm$ 0.4         | 7.5 $\pm$ 0.5         | 8.7 $\pm$ 0.2  | 9.0 $\pm$ 0.1            | 6.6 $\pm$ 0.2     | 7.1 $\pm$ 0.5      | 8.1 $\pm$ 0.5    | 8.0 $\pm$ 0.4    | 8.7 $\pm$ 0.2 |
| o1-preview-2024-09-12                    | **408.5** | 7.0 $\pm$ 0.6               | 7.8 $\pm$ 0.4         | 8.6 $\pm$ 0.4            | 9.4 $\pm$ 0.2 | 7.9 $\pm$ 0.2                 | 7.9 $\pm$ 0.4                  | 7.5 $\pm$ 0.5         | 6.8 $\pm$ 1.0         | 8.8 $\pm$ 0.2  | 8.2 $\pm$ 0.2            | 6.1 $\pm$ 0.6     | 6.5 $\pm$ 0.4      | 7.6 $\pm$ 0.5    | 7.9 $\pm$ 0.5    | 8.8 $\pm$ 0.2 |
| o3-mini-20250131-HIGH                    | **406.9** | 7.4 $\pm$ 0.7               | 7.2 $\pm$ 0.9         | 8.9 $\pm$ 0.2            | 9.6 $\pm$ 0.2 | 7.5 $\pm$ 0.5                 | 7.9 $\pm$ 0.4                  | 7.6 $\pm$ 0.4         | 7.0 $\pm$ 0.7         | 8.7 $\pm$ 0.2  | 8.2 $\pm$ 0.2            | 5.9 $\pm$ 0.6     | 6.1 $\pm$ 0.6      | 7.6 $\pm$ 0.4    | 7.4 $\pm$ 0.8    | 8.6 $\pm$ 0.4 |
| qwen2.5-32b-instruct                     | **406.5** | 6.4 $\pm$ 0.5               | 7.5 $\pm$ 0.4         | 8.8 $\pm$ 0.4            | 9.2 $\pm$ 0.2 | 7.6 $\pm$ 0.4                 | 7.6 $\pm$ 0.4                  | 7.6 $\pm$ 0.6         | 6.5 $\pm$ 0.4         | 8.4 $\pm$ 0.4  | 8.5 $\pm$ 0.6            | 6.0 $\pm$ 0.4     | 6.6 $\pm$ 0.4      | 7.2 $\pm$ 0.2    | 7.9 $\pm$ 0.6    | 8.2 $\pm$ 0.2 |
| mistral-large-2407                       | **406.5** | 7.2 $\pm$ 0.8               | 7.5 $\pm$ 0.9         | 8.8 $\pm$ 0.6            | 9.4 $\pm$ 0.3 | 7.6 $\pm$ 0.2                 | 7.8 $\pm$ 0.8                  | 8.0 $\pm$ 0.4         | 6.8 $\pm$ 0.8         | 8.6 $\pm$ 0.6  | 8.6 $\pm$ 0.2            | 5.9 $\pm$ 0.7     | 6.9 $\pm$ 0.4      | 7.5 $\pm$ 0.6    | 7.5 $\pm$ 0.5    | 8.6 $\pm$ 0.4 |
| qwen2.5-72b-instruct                     | **404.6** | 6.8 $\pm$ 0.8               | 7.5 $\pm$ 0.0         | 8.8 $\pm$ 0.2            | 9.2 $\pm$ 0.2 | 8.0 $\pm$ 0.1                 | 7.9 $\pm$ 0.4                  | 7.1 $\pm$ 0.2         | 7.0 $\pm$ 0.6         | 8.2 $\pm$ 0.2  | 8.6 $\pm$ 0.4            | 6.1 $\pm$ 0.9     | 6.7 $\pm$ 0.2      | 7.6 $\pm$ 0.4    | 7.8 $\pm$ 0.2    | 8.2 $\pm$ 0.6 |
| gpt-4-0613                               | **403.0** | 7.9 $\pm$ 0.5               | 6.6 $\pm$ 0.4         | 9.0 $\pm$ 0.4            | 9.5 $\pm$ 0.5 | 7.4 $\pm$ 0.2                 | 8.2 $\pm$ 0.2                  | 7.6 $\pm$ 0.2         | 7.4 $\pm$ 0.2         | 8.9 $\pm$ 0.4  | 8.6 $\pm$ 0.6            | 5.8 $\pm$ 1.6     | 6.8 $\pm$ 0.2      | 8.0 $\pm$ 0.4    | 7.1 $\pm$ 0.4    | 8.8 $\pm$ 0.2 |
| qwen-plus-2025-01-25                     | **401.0** | 7.2 $\pm$ 0.6               | 7.4 $\pm$ 0.4         | 8.9 $\pm$ 0.2            | 9.6 $\pm$ 0.4 | 7.2 $\pm$ 0.6                 | 7.8 $\pm$ 0.2                  | 7.8 $\pm$ 0.6         | 7.2 $\pm$ 0.4         | 8.5 $\pm$ 0.4  | 8.5 $\pm$ 0.4            | 6.8 $\pm$ 0.9     | 6.8 $\pm$ 0.2      | 7.6 $\pm$ 0.6    | 7.1 $\pm$ 0.6    | 8.6 $\pm$ 0.4 |
| falcon37b-instruct-q8_0                  | **399.1** | 7.2 $\pm$ 0.6               | 7.2 $\pm$ 0.5         | 9.0 $\pm$ 0.5            | 9.4 $\pm$ 0.4 | 8.0 $\pm$ 0.4                 | 7.9 $\pm$ 0.4                  | 6.8 $\pm$ 0.2         | 6.9 $\pm$ 0.5         | 8.7 $\pm$ 0.3  | 8.4 $\pm$ 0.2            | 6.0 $\pm$ 0.0     | 6.7 $\pm$ 0.3      | 8.0 $\pm$ 0.6    | 7.3 $\pm$ 0.4    | 8.2 $\pm$ 0.4 |
| open-mistral-nemo                        | **399.0** | 6.8 $\pm$ 0.4               | 7.4 $\pm$ 0.4         | 8.5 $\pm$ 0.5            | 9.2 $\pm$ 0.2 | 7.5 $\pm$ 0.4                 | 7.8 $\pm$ 0.6                  | 7.5 $\pm$ 0.4         | 6.8 $\pm$ 0.2         | 8.5 $\pm$ 0.4  | 8.4 $\pm$ 0.2            | 5.8 $\pm$ 0.6     | 6.9 $\pm$ 0.4      | 7.6 $\pm$ 0.6    | 7.1 $\pm$ 0.4    | 8.1 $\pm$ 0.2 |
| ministral-8b-2410                        | **399.0** | 7.1 $\pm$ 0.7               | 7.1 $\pm$ 0.6         | 8.9 $\pm$ 0.2            | 9.1 $\pm$ 0.4 | 7.1 $\pm$ 0.7                 | 7.4 $\pm$ 0.2                  | 7.8 $\pm$ 0.6         | 7.6 $\pm$ 0.7         | 8.6 $\pm$ 0.4  | 8.4 $\pm$ 0.2            | 6.8 $\pm$ 0.8     | 6.6 $\pm$ 0.2      | 7.8 $\pm$ 0.4    | 7.4 $\pm$ 1.0    | 8.6 $\pm$ 0.4 |
| falcon33b-instruct-q8_0                  | **398.9** | 7.6 $\pm$ 0.4               | 7.1 $\pm$ 0.6         | 8.8 $\pm$ 0.4            | 9.6 $\pm$ 0.2 | 6.9 $\pm$ 0.2                 | 7.8 $\pm$ 0.6                  | 7.3 $\pm$ 0.5         | 7.7 $\pm$ 0.8         | 8.9 $\pm$ 0.4  | 8.4 $\pm$ 0.4            | 6.6 $\pm$ 0.5     | 6.7 $\pm$ 0.5      | 7.8 $\pm$ 0.2    | 7.2 $\pm$ 0.2    | 8.7 $\pm$ 0.2 |
| mistral-large-2411                       | **397.6** | 7.4 $\pm$ 1.1               | 7.2 $\pm$ 0.5         | 8.7 $\pm$ 0.4            | 9.6 $\pm$ 0.3 | 7.5 $\pm$ 0.6                 | 7.9 $\pm$ 0.3                  | 7.2 $\pm$ 0.7         | 7.0 $\pm$ 0.6         | 8.8 $\pm$ 0.4  | 8.3 $\pm$ 0.3            | 6.2 $\pm$ 1.0     | 6.8 $\pm$ 0.6      | 7.8 $\pm$ 0.4    | 7.2 $\pm$ 0.5    | 8.3 $\pm$ 0.4 |
| qwen2.5-14b-instruct-1m                  | **397.4** | 7.8 $\pm$ 0.4               | 7.6 $\pm$ 0.7         | 8.7 $\pm$ 0.2            | 9.0 $\pm$ 0.4 | 7.8 $\pm$ 0.2                 | 7.7 $\pm$ 0.5                  | 7.5 $\pm$ 0.3         | 7.2 $\pm$ 0.4         | 8.4 $\pm$ 0.2  | 8.7 $\pm$ 0.2            | 6.6 $\pm$ 0.2     | 6.8 $\pm$ 0.8      | 7.8 $\pm$ 0.7    | 7.6 $\pm$ 0.4    | 8.4 $\pm$ 0.2 |
| ministral-3b-2410                        | **396.9** | 7.5 $\pm$ 0.4               | 7.5 $\pm$ 0.6         | 8.6 $\pm$ 0.4            | 9.2 $\pm$ 0.6 | 7.5 $\pm$ 0.6                 | 7.6 $\pm$ 0.4                  | 7.6 $\pm$ 0.7         | 7.1 $\pm$ 0.2         | 8.7 $\pm$ 0.2  | 8.4 $\pm$ 0.4            | 6.4 $\pm$ 0.2     | 7.2 $\pm$ 0.4      | 7.9 $\pm$ 0.3    | 7.6 $\pm$ 0.6    | 8.4 $\pm$ 0.4 |
| qwen2.5-7b-instruct-1m                   | **395.8** | 7.8 $\pm$ 0.2               | 7.4 $\pm$ 0.7         | 8.6 $\pm$ 0.4            | 9.2 $\pm$ 0.2 | 7.4 $\pm$ 0.6                 | 7.6 $\pm$ 0.7                  | 7.4 $\pm$ 0.2         | 7.5 $\pm$ 0.8         | 8.6 $\pm$ 0.4  | 8.4 $\pm$ 0.4            | 6.6 $\pm$ 0.4     | 6.8 $\pm$ 0.2      | 7.9 $\pm$ 0.2    | 7.2 $\pm$ 0.4    | 8.6 $\pm$ 0.4 |
| mistral-small-2501                       | **394.1** | 6.7 $\pm$ 1.0               | 7.4 $\pm$ 0.8         | 8.7 $\pm$ 0.7            | 9.2 $\pm$ 0.7 | 7.4 $\pm$ 0.5                 | 7.4 $\pm$ 1.0                  | 7.5 $\pm$ 0.4         | 6.6 $\pm$ 1.1         | 8.4 $\pm$ 0.6  | 8.0 $\pm$ 0.7            | 6.8 $\pm$ 0.6     | 6.8 $\pm$ 0.6      | 7.3 $\pm$ 0.7    | 7.3 $\pm$ 0.6    | 8.2 $\pm$ 0.7 |
| mistral-small-2409                       | **394.0** | 6.5 $\pm$ 1.1               | 7.1 $\pm$ 0.4         | 8.4 $\pm$ 0.2            | 9.0 $\pm$ 0.0 | 7.2 $\pm$ 0.6                 | 7.2 $\pm$ 0.6                  | 7.5 $\pm$ 0.4         | 6.6 $\pm$ 0.4         | 8.4 $\pm$ 0.2  | 8.5 $\pm$ 0.4            | 6.0 $\pm$ 0.6     | 6.8 $\pm$ 0.6      | 7.2 $\pm$ 0.2    | 7.1 $\pm$ 0.7    | 7.9 $\pm$ 0.2 |
| deepseek-aiDeepSeek-R1-Distill-Llama-70B | **393.3** | 8.2 $\pm$ 0.6               | 7.0 $\pm$ 0.4         | 8.8 $\pm$ 0.2            | 9.2 $\pm$ 0.2 | 7.2 $\pm$ 0.8                 | 7.6 $\pm$ 0.5                  | 7.4 $\pm$ 0.3         | 7.6 $\pm$ 1.1         | 8.6 $\pm$ 0.2  | 8.2 $\pm$ 0.6            | 6.9 $\pm$ 0.2     | 6.9 $\pm$ 0.6      | 7.8 $\pm$ 0.4    | 7.6 $\pm$ 0.9    | 8.6 $\pm$ 0.2 |
| qwen-max-2025-01-25                      | **393.0** | 7.9 $\pm$ 1.1               | 7.0 $\pm$ 0.4         | 8.8 $\pm$ 0.4            | 9.4 $\pm$ 0.2 | 7.6 $\pm$ 0.2                 | 7.4 $\pm$ 0.6                  | 7.8 $\pm$ 0.2         | 6.8 $\pm$ 1.0         | 8.6 $\pm$ 0.2  | 8.4 $\pm$ 0.5            | 7.0 $\pm$ 0.6     | 6.6 $\pm$ 0.4      | 7.8 $\pm$ 0.4    | 7.4 $\pm$ 0.2    | 8.5 $\pm$ 0.4 |
| gpt-4o-mini-2024-07-18                   | **392.4** | 7.6 $\pm$ 0.4               | 6.7 $\pm$ 0.3         | 8.6 $\pm$ 0.4            | 9.4 $\pm$ 0.2 | 7.5 $\pm$ 0.4                 | 7.6 $\pm$ 0.4                  | 7.0 $\pm$ 0.7         | 7.5 $\pm$ 0.5         | 8.5 $\pm$ 0.1  | 8.2 $\pm$ 0.4            | 6.6 $\pm$ 0.6     | 7.1 $\pm$ 0.4      | 7.8 $\pm$ 0.2    | 7.6 $\pm$ 0.4    | 8.6 $\pm$ 0.1 |
| deepseek-aiDeepSeek-R1-Zero              | **391.0** | 7.8 $\pm$ 0.2               | 7.1 $\pm$ 0.6         | 8.9 $\pm$ 0.2            | 8.6 $\pm$ 0.5 | 7.4 $\pm$ 0.4                 | 7.6 $\pm$ 0.5                  | 7.0 $\pm$ 0.4         | 7.5 $\pm$ 0.0         | 8.5 $\pm$ 0.4  | 8.6 $\pm$ 0.2            | 6.6 $\pm$ 0.2     | 6.9 $\pm$ 0.8      | 7.9 $\pm$ 0.2    | 7.1 $\pm$ 0.9    | 8.5 $\pm$ 0.4 |
| nvidiaLlama-3.1-Nemotron-70B-Instruct    | **390.6** | 8.1 $\pm$ 0.4               | 6.6 $\pm$ 0.2         | 9.0 $\pm$ 0.4            | 9.4 $\pm$ 0.3 | 7.7 $\pm$ 0.3                 | 7.3 $\pm$ 0.3                  | 7.3 $\pm$ 0.9         | 7.4 $\pm$ 0.8         | 8.5 $\pm$ 0.4  | 8.5 $\pm$ 0.4            | 6.9 $\pm$ 0.2     | 7.4 $\pm$ 0.6      | 7.7 $\pm$ 0.3    | 7.5 $\pm$ 0.5    | 8.5 $\pm$ 0.0 |
| gemini-exp-1206                          | **390.5** | 7.9 $\pm$ 0.4               | 6.9 $\pm$ 0.7         | 8.6 $\pm$ 0.6            | 9.9 $\pm$ 0.2 | 6.9 $\pm$ 0.2                 | 7.8 $\pm$ 0.8                  | 7.0 $\pm$ 0.8         | 7.4 $\pm$ 0.6         | 8.8 $\pm$ 0.8  | 8.1 $\pm$ 0.6            | 6.5 $\pm$ 0.8     | 7.0 $\pm$ 0.7      | 7.5 $\pm$ 0.0    | 6.6 $\pm$ 0.5    | 8.6 $\pm$ 0.4 |
| googlegemma-2-9b-it                      | **390.1** | 8.2 $\pm$ 0.6               | 7.0 $\pm$ 0.5         | 8.4 $\pm$ 0.4            | 9.5 $\pm$ 0.4 | 7.1 $\pm$ 0.2                 | 7.4 $\pm$ 0.7                  | 7.4 $\pm$ 0.5         | 7.3 $\pm$ 0.8         | 8.8 $\pm$ 0.2  | 8.4 $\pm$ 0.3            | 7.0 $\pm$ 0.8     | 6.7 $\pm$ 0.5      | 7.9 $\pm$ 0.5    | 7.3 $\pm$ 0.2    | 8.7 $\pm$ 0.2 |
| gemini-2.0-flash-exp                     | **389.5** | 7.8 $\pm$ 0.4               | 6.7 $\pm$ 0.9         | 8.6 $\pm$ 0.4            | 9.2 $\pm$ 0.2 | 7.2 $\pm$ 0.4                 | 7.1 $\pm$ 0.6                  | 7.2 $\pm$ 0.8         | 7.6 $\pm$ 0.3         | 8.4 $\pm$ 0.3  | 8.0 $\pm$ 0.4            | 6.4 $\pm$ 0.6     | 6.5 $\pm$ 0.4      | 7.6 $\pm$ 0.4    | 7.2 $\pm$ 0.6    | 8.4 $\pm$ 0.2 |
| gemini-1.5-flash-002                     | **388.5** | 8.0 $\pm$ 0.4               | 7.1 $\pm$ 0.7         | 8.8 $\pm$ 0.5            | 9.8 $\pm$ 0.2 | 7.5 $\pm$ 0.4                 | 6.8 $\pm$ 1.2                  | 7.4 $\pm$ 1.0         | 7.7 $\pm$ 0.3         | 8.0 $\pm$ 0.8  | 8.6 $\pm$ 0.6            | 6.8 $\pm$ 0.2     | 6.6 $\pm$ 0.6      | 8.3 $\pm$ 0.5    | 6.8 $\pm$ 1.0    | 8.4 $\pm$ 0.4 |
| o1-pro-2024-12-05                        | **387.0** | 7.6 $\pm$ 0.4               | 6.6 $\pm$ 0.2         | 8.8 $\pm$ 0.2            | 9.4 $\pm$ 0.4 | 7.0 $\pm$ 0.4                 | 7.4 $\pm$ 0.4                  | 7.0 $\pm$ 0.8         | 7.6 $\pm$ 0.2         | 8.8 $\pm$ 0.6  | 8.0 $\pm$ 0.4            | 6.4 $\pm$ 0.6     | 6.5 $\pm$ 0.4      | 8.1 $\pm$ 0.2    | 6.6 $\pm$ 0.4    | 8.2 $\pm$ 0.6 |
| o1-2024-12-05                            | **386.6** | 8.2 $\pm$ 0.6               | 6.7 $\pm$ 0.5         | 8.9 $\pm$ 0.2            | 9.3 $\pm$ 0.6 | 7.2 $\pm$ 0.8                 | 7.2 $\pm$ 0.5                  | 7.6 $\pm$ 0.2         | 7.6 $\pm$ 0.9         | 8.8 $\pm$ 0.4  | 8.3 $\pm$ 0.4            | 7.0 $\pm$ 0.4     | 7.0 $\pm$ 0.3      | 7.9 $\pm$ 0.5    | 6.8 $\pm$ 0.8    | 8.4 $\pm$ 0.2 |
| Gemini-1.5-Pro-Exp-0801                  | **386.0** | 8.4 $\pm$ 0.2               | 6.6 $\pm$ 0.4         | 8.8 $\pm$ 0.4            | 9.8 $\pm$ 0.2 | 7.6 $\pm$ 0.5                 | 6.5 $\pm$ 0.7                  | 7.4 $\pm$ 0.4         | 7.6 $\pm$ 0.4         | 8.4 $\pm$ 0.5  | 8.8 $\pm$ 0.2            | 7.6 $\pm$ 1.0     | 6.6 $\pm$ 0.5      | 7.9 $\pm$ 0.2    | 7.0 $\pm$ 0.6    | 8.6 $\pm$ 0.4 |
| deepseek-aiDeepSeek-V3                   | **385.5** | 7.9 $\pm$ 0.6               | 6.6 $\pm$ 0.2         | 8.6 $\pm$ 0.4            | 9.4 $\pm$ 0.2 | 7.2 $\pm$ 0.2                 | 7.4 $\pm$ 0.8                  | 7.2 $\pm$ 0.2         | 7.5 $\pm$ 0.9         | 8.5 $\pm$ 0.0  | 8.1 $\pm$ 0.5            | 6.5 $\pm$ 0.0     | 6.9 $\pm$ 0.5      | 7.9 $\pm$ 0.5    | 6.9 $\pm$ 0.5    | 8.0 $\pm$ 0.4 |
| deepseek-aiDeepSeek-R1                   | **385.4** | 8.4 $\pm$ 0.2               | 7.1 $\pm$ 0.2         | 9.0 $\pm$ 0.0            | 9.5 $\pm$ 0.0 | 7.0 $\pm$ 0.5                 | 7.6 $\pm$ 0.6                  | 7.3 $\pm$ 0.4         | 8.0 $\pm$ 0.4         | 8.4 $\pm$ 0.3  | 8.4 $\pm$ 0.3            | 7.4 $\pm$ 0.3     | 7.5 $\pm$ 0.5      | 8.2 $\pm$ 0.2    | 6.8 $\pm$ 0.5    | 8.7 $\pm$ 0.3 |
| chatgpt-4o-latest-2024-11-20             | **381.0** | 7.6 $\pm$ 0.6               | 6.8 $\pm$ 0.2         | 8.6 $\pm$ 0.2            | 9.4 $\pm$ 0.4 | 6.6 $\pm$ 0.5                 | 7.0 $\pm$ 0.6                  | 6.8 $\pm$ 0.2         | 8.0 $\pm$ 0.4         | 8.5 $\pm$ 0.7  | 8.0 $\pm$ 0.4            | 6.8 $\pm$ 0.8     | 6.6 $\pm$ 0.4      | 7.8 $\pm$ 0.4    | 6.2 $\pm$ 0.6    | 8.1 $\pm$ 0.2 |
| gemini-1.5-flash-8b                      | **380.8** | 8.6 $\pm$ 0.7               | 6.5 $\pm$ 0.5         | 8.8 $\pm$ 0.2            | 9.7 $\pm$ 0.2 | 6.9 $\pm$ 0.2                 | 7.6 $\pm$ 0.2                  | 7.4 $\pm$ 0.3         | 7.9 $\pm$ 0.8         | 8.1 $\pm$ 0.2  | 8.7 $\pm$ 0.2            | 7.1 $\pm$ 0.6     | 7.4 $\pm$ 0.8      | 8.4 $\pm$ 0.5    | 6.6 $\pm$ 0.9    | 8.6 $\pm$ 0.3 |
| o1-2024-12-17                            | **379.8** | 8.0 $\pm$ 0.7               | 6.8 $\pm$ 0.4         | 8.6 $\pm$ 0.4            | 9.4 $\pm$ 0.2 | 6.4 $\pm$ 0.7                 | 7.0 $\pm$ 0.0                  | 7.3 $\pm$ 0.8         | 7.8 $\pm$ 0.2         | 8.8 $\pm$ 0.3  | 8.2 $\pm$ 0.2            | 7.2 $\pm$ 0.6     | 6.8 $\pm$ 0.6      | 7.9 $\pm$ 0.5    | 6.0 $\pm$ 0.7    | 8.6 $\pm$ 0.4 |
| DeepSeek-R1-Lite-Preview                 | **379.5** | 8.0 $\pm$ 0.8               | 6.6 $\pm$ 0.5         | 8.2 $\pm$ 0.2            | 8.5 $\pm$ 0.6 | 7.0 $\pm$ 0.4                 | 6.9 $\pm$ 0.7                  | 6.9 $\pm$ 0.2         | 7.5 $\pm$ 0.6         | 8.4 $\pm$ 0.4  | 8.4 $\pm$ 0.2            | 6.4 $\pm$ 0.4     | 7.0 $\pm$ 0.4      | 7.5 $\pm$ 0.4    | 7.0 $\pm$ 0.0    | 8.4 $\pm$ 0.2 |
| gemini-2.0-pro-exp-02-05                 | **378.5** | 7.6 $\pm$ 1.0               | 6.8 $\pm$ 1.0         | 8.2 $\pm$ 0.8            | 9.4 $\pm$ 0.4 | 7.0 $\pm$ 0.4                 | 6.6 $\pm$ 0.5                  | 6.1 $\pm$ 0.6         | 7.5 $\pm$ 0.6         | 8.4 $\pm$ 0.5  | 8.2 $\pm$ 0.2            | 7.1 $\pm$ 0.4     | 6.4 $\pm$ 0.5      | 7.4 $\pm$ 0.4    | 6.8 $\pm$ 0.6    | 8.1 $\pm$ 0.4 |
| meta-llamaLlama-3.2-3B-Instruct          | **377.4** | 7.8 $\pm$ 0.2               | 6.6 $\pm$ 0.2         | 8.4 $\pm$ 0.2            | 9.0 $\pm$ 0.4 | 6.9 $\pm$ 0.2                 | 7.0 $\pm$ 0.4                  | 6.7 $\pm$ 0.6         | 7.9 $\pm$ 0.2         | 8.4 $\pm$ 0.4  | 8.3 $\pm$ 0.5            | 7.2 $\pm$ 0.2     | 7.0 $\pm$ 0.4      | 7.8 $\pm$ 0.5    | 6.9 $\pm$ 0.6    | 8.2 $\pm$ 0.2 |
| qwq32b-preview-q4_K_M                    | **376.5** | 7.0 $\pm$ 1.5               | 6.6 $\pm$ 1.1         | 8.2 $\pm$ 1.0            | 7.8 $\pm$ 0.2 | 6.9 $\pm$ 1.0                 | 7.0 $\pm$ 0.7                  | 6.6 $\pm$ 0.7         | 6.9 $\pm$ 1.0         | 8.0 $\pm$ 0.6  | 8.1 $\pm$ 0.6            | 6.1 $\pm$ 1.3     | 6.5 $\pm$ 1.4      | 7.0 $\pm$ 0.8    | 6.8 $\pm$ 1.1    | 7.9 $\pm$ 0.7 |
| gemini-exp-1114                          | **372.3** | 8.2 $\pm$ 0.5               | 6.9 $\pm$ 0.5         | 8.0 $\pm$ 0.6            | 9.0 $\pm$ 0.0 | 6.5 $\pm$ 0.4                 | 6.8 $\pm$ 0.4                  | 7.0 $\pm$ 0.4         | 8.2 $\pm$ 0.3         | 8.1 $\pm$ 0.4  | 8.8 $\pm$ 0.2            | 7.2 $\pm$ 0.6     | 7.0 $\pm$ 0.4      | 8.3 $\pm$ 0.4    | 6.4 $\pm$ 0.6    | 8.3 $\pm$ 0.5 |
| meta-llamaLlama-3.2-1B-Instruct          | **371.0** | 7.4 $\pm$ 0.7               | 6.1 $\pm$ 0.7         | 7.8 $\pm$ 1.0            | 9.0 $\pm$ 0.4 | 7.0 $\pm$ 0.4                 | 6.8 $\pm$ 1.0                  | 5.8 $\pm$ 0.6         | 7.5 $\pm$ 0.4         | 7.5 $\pm$ 0.8  | 8.1 $\pm$ 0.2            | 6.5 $\pm$ 0.6     | 6.5 $\pm$ 0.6      | 6.9 $\pm$ 0.5    | 6.9 $\pm$ 0.6    | 7.6 $\pm$ 0.7 |
| o1-pro-2024-12-17                        | **369.8** | 8.0 $\pm$ 0.5               | 6.8 $\pm$ 0.2         | 8.5 $\pm$ 0.5            | 9.2 $\pm$ 0.2 | 7.0 $\pm$ 0.8                 | 7.2 $\pm$ 1.0                  | 6.9 $\pm$ 0.6         | 7.0 $\pm$ 1.2         | 8.0 $\pm$ 0.6  | 7.9 $\pm$ 0.9            | 7.1 $\pm$ 1.0     | 7.0 $\pm$ 0.9      | 8.4 $\pm$ 0.4    | 6.2 $\pm$ 0.9    | 8.3 $\pm$ 0.8 |
| gpt-4-1106-preview                       | **369.8** | 8.0 $\pm$ 0.4               | 6.8 $\pm$ 0.3         | 7.8 $\pm$ 0.2            | 9.0 $\pm$ 0.1 | 6.8 $\pm$ 0.2                 | 7.0 $\pm$ 0.5                  | 6.5 $\pm$ 0.5         | 7.1 $\pm$ 0.9         | 7.8 $\pm$ 0.6  | 7.6 $\pm$ 0.4            | 7.1 $\pm$ 0.4     | 6.3 $\pm$ 0.3      | 7.4 $\pm$ 0.4    | 7.0 $\pm$ 0.4    | 7.8 $\pm$ 0.4 |
| meta-llamaLlama-3.3-70B-Instruct         | **369.1** | 8.5 $\pm$ 0.4               | 5.7 $\pm$ 0.4         | 8.3 $\pm$ 0.6            | 9.2 $\pm$ 0.2 | 7.0 $\pm$ 0.4                 | 6.3 $\pm$ 0.5                  | 6.9 $\pm$ 0.2         | 8.0 $\pm$ 0.4         | 8.2 $\pm$ 0.5  | 8.2 $\pm$ 0.7            | 7.9 $\pm$ 0.4     | 6.5 $\pm$ 0.6      | 7.9 $\pm$ 0.7    | 7.0 $\pm$ 0.8    | 8.2 $\pm$ 0.2 |
| googlegemma-2-2b-it                      | **368.5** | 8.1 $\pm$ 0.2               | 6.0 $\pm$ 0.6         | 8.0 $\pm$ 0.6            | 9.1 $\pm$ 0.2 | 7.1 $\pm$ 0.4                 | 6.9 $\pm$ 0.4                  | 6.5 $\pm$ 0.4         | 7.8 $\pm$ 0.2         | 8.4 $\pm$ 0.2  | 8.1 $\pm$ 0.7            | 7.4 $\pm$ 0.4     | 6.6 $\pm$ 0.4      | 8.2 $\pm$ 0.4    | 6.5 $\pm$ 0.7    | 8.1 $\pm$ 0.4 |
| meta-llamaMeta-Llama-3.1-405B-Instruct   | **368.0** | 8.1 $\pm$ 0.4               | 5.8 $\pm$ 0.8         | 8.2 $\pm$ 0.8            | 9.5 $\pm$ 0.0 | 7.0 $\pm$ 0.4                 | 6.5 $\pm$ 0.4                  | 6.5 $\pm$ 0.6         | 7.8 $\pm$ 0.4         | 8.1 $\pm$ 0.4  | 8.0 $\pm$ 0.4            | 7.2 $\pm$ 0.4     | 6.6 $\pm$ 0.4      | 7.9 $\pm$ 0.5    | 6.6 $\pm$ 0.6    | 7.9 $\pm$ 0.5 |
| gpt-4o-mini-2024-11-05                   | **364.1** | 7.6 $\pm$ 0.2               | 6.4 $\pm$ 0.2         | 8.4 $\pm$ 0.2            | 9.2 $\pm$ 0.2 | 6.0 $\pm$ 0.6                 | 6.4 $\pm$ 0.4                  | 7.0 $\pm$ 0.4         | 7.2 $\pm$ 0.3         | 8.1 $\pm$ 0.1  | 8.0 $\pm$ 0.0            | 7.1 $\pm$ 0.2     | 6.8 $\pm$ 0.6      | 8.0 $\pm$ 0.5    | 6.4 $\pm$ 0.9    | 7.5 $\pm$ 0.4 |
| gemini-2.0-flash-lite-preview-02-05      | **362.0** | 8.1 $\pm$ 0.6               | 6.2 $\pm$ 0.8         | 8.5 $\pm$ 0.5            | 9.5 $\pm$ 0.0 | 6.6 $\pm$ 0.5                 | 6.1 $\pm$ 0.7                  | 6.0 $\pm$ 1.3         | 8.1 $\pm$ 0.6         | 8.4 $\pm$ 0.4  | 7.4 $\pm$ 0.5            | 7.5 $\pm$ 0.4     | 6.4 $\pm$ 0.8      | 8.1 $\pm$ 0.2    | 6.1 $\pm$ 0.5    | 7.6 $\pm$ 0.9 |
| Gemini-1.5-Pro-Exp-0827                  | **361.5** | 8.8 $\pm$ 0.4               | 5.9 $\pm$ 0.8         | 8.0 $\pm$ 0.4            | 9.5 $\pm$ 0.4 | 6.8 $\pm$ 0.8                 | 5.9 $\pm$ 0.7                  | 6.0 $\pm$ 1.2         | 8.2 $\pm$ 0.2         | 7.8 $\pm$ 0.6  | 8.1 $\pm$ 0.6            | 6.9 $\pm$ 0.9     | 6.2 $\pm$ 0.8      | 8.0 $\pm$ 0.6    | 6.6 $\pm$ 0.4    | 7.5 $\pm$ 0.6 |
| gemini-2.0-flash-thinking-exp-01-21      | **360.6** | 8.4 $\pm$ 0.4               | 5.8 $\pm$ 1.4         | 7.6 $\pm$ 0.7            | 9.3 $\pm$ 0.2 | 6.6 $\pm$ 1.0                 | 6.4 $\pm$ 0.4                  | 6.4 $\pm$ 0.7         | 7.9 $\pm$ 0.3         | 8.0 $\pm$ 0.7  | 7.3 $\pm$ 0.7            | 7.2 $\pm$ 0.5     | 6.5 $\pm$ 0.6      | 7.6 $\pm$ 0.4    | 6.4 $\pm$ 0.6    | 8.0 $\pm$ 0.6 |
| meta-llamaMeta-Llama-3.1-70B-Instruct    | **358.9** | 8.0 $\pm$ 0.8               | 6.0 $\pm$ 0.5         | 8.1 $\pm$ 0.4            | 9.5 $\pm$ 0.0 | 6.4 $\pm$ 0.5                 | 6.4 $\pm$ 0.2                  | 6.2 $\pm$ 0.8         | 7.4 $\pm$ 0.4         | 7.7 $\pm$ 0.4  | 8.2 $\pm$ 0.6            | 7.4 $\pm$ 0.4     | 7.0 $\pm$ 0.4      | 7.7 $\pm$ 0.3    | 6.0 $\pm$ 0.5    | 7.8 $\pm$ 0.4 |
| meta-llamaMeta-Llama-3.1-8B-Instruct     | **355.0** | 8.2 $\pm$ 0.6               | 6.3 $\pm$ 0.3         | 8.2 $\pm$ 0.7            | 9.7 $\pm$ 0.2 | 6.1 $\pm$ 0.7                 | 5.7 $\pm$ 1.3                  | 6.3 $\pm$ 0.5         | 7.6 $\pm$ 0.4         | 7.7 $\pm$ 0.7  | 8.1 $\pm$ 0.7            | 7.3 $\pm$ 0.6     | 7.2 $\pm$ 1.2      | 8.0 $\pm$ 0.7    | 5.7 $\pm$ 1.0    | 8.0 $\pm$ 0.4 |
| chatgpt-4o-latest-2025-01-29             | **353.5** | 8.1 $\pm$ 0.4               | 6.2 $\pm$ 0.4         | 7.8 $\pm$ 0.2            | 9.2 $\pm$ 0.2 | 6.4 $\pm$ 0.4                 | 6.2 $\pm$ 0.6                  | 6.4 $\pm$ 0.4         | 7.8 $\pm$ 0.6         | 8.0 $\pm$ 0.4  | 7.4 $\pm$ 0.4            | 7.5 $\pm$ 0.4     | 7.1 $\pm$ 0.4      | 8.0 $\pm$ 0.7    | 6.2 $\pm$ 0.4    | 7.5 $\pm$ 0.6 |
| googlegemma-2-27b-it                     | **289.5** | 8.6 $\pm$ 0.4               | 4.9 $\pm$ 1.2         | 7.0 $\pm$ 0.6            | 8.6 $\pm$ 0.4 | 4.8 $\pm$ 0.8                 | 5.0 $\pm$ 1.2                  | 4.9 $\pm$ 0.4         | 8.0 $\pm$ 0.4         | 5.4 $\pm$ 1.0  | 6.8 $\pm$ 0.2            | 8.4 $\pm$ 0.4     | 6.6 $\pm$ 0.4      | 8.8 $\pm$ 0.4    | 3.8 $\pm$ 0.6    | 5.8 $\pm$ 1.0 |
## Individual Results


### gpt-4o-mini-2024-07-18


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.4      |
| Emotional Stability          | 6.7 $\pm$ 0.3      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.4      |
| Conflict Resolution          | 7.0 $\pm$ 0.7      |
| Work-related Stress          | 7.5 $\pm$ 0.5      |
| Adaptability                 | 8.5 $\pm$ 0.1      |
| Achievement Motivation       | 8.2 $\pm$ 0.4      |
| Fear of Failure              | 6.6 $\pm$ 0.6      |
| Need for Control             | 7.1 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.2      |
| Social Support               | 7.6 $\pm$ 0.4      |
| Resilience                   | 8.6 $\pm$ 0.1      |






### gpt-4o-2024-05-13


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.1 $\pm$ 0.6      |
| Emotional Stability          | 7.8 $\pm$ 0.5      |
| Problem-solving Skills       | 9.0 $\pm$ 0.4      |
| Creativity                   | 9.6 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.3 $\pm$ 0.5      |
| Confidence and Self-efficacy | 8.2 $\pm$ 0.3      |
| Conflict Resolution          | 8.1 $\pm$ 0.6      |
| Work-related Stress          | 6.9 $\pm$ 0.3      |
| Adaptability                 | 8.8 $\pm$ 0.4      |
| Achievement Motivation       | 8.6 $\pm$ 0.4      |
| Fear of Failure              | 5.7 $\pm$ 0.5      |
| Need for Control             | 6.6 $\pm$ 0.2      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 8.0 $\pm$ 0.7      |
| Resilience                   | 8.7 $\pm$ 0.5      |






### gpt-4-turbo-2024-04-09


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.9 $\pm$ 0.7      |
| Emotional Stability          | 7.9 $\pm$ 0.2      |
| Problem-solving Skills       | 9.1 $\pm$ 0.2      |
| Creativity                   | 9.8 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.1 $\pm$ 0.4      |
| Conflict Resolution          | 7.9 $\pm$ 0.4      |
| Work-related Stress          | 7.2 $\pm$ 0.8      |
| Adaptability                 | 9.0 $\pm$ 0.0      |
| Achievement Motivation       | 8.8 $\pm$ 0.2      |
| Fear of Failure              | 6.6 $\pm$ 0.5      |
| Need for Control             | 7.1 $\pm$ 0.4      |
| Cognitive Load               | 7.5 $\pm$ 0.6      |
| Social Support               | 7.6 $\pm$ 0.4      |
| Resilience                   | 8.8 $\pm$ 0.2      |






### gpt-4-0125-preview


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.8 $\pm$ 1.0      |
| Emotional Stability          | 7.4 $\pm$ 0.6      |
| Problem-solving Skills       | 8.7 $\pm$ 0.4      |
| Creativity                   | 9.6 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.8      |
| Confidence and Self-efficacy | 8.2 $\pm$ 0.3      |
| Conflict Resolution          | 7.7 $\pm$ 0.7      |
| Work-related Stress          | 6.8 $\pm$ 0.7      |
| Adaptability                 | 8.6 $\pm$ 0.4      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 5.8 $\pm$ 0.8      |
| Need for Control             | 6.6 $\pm$ 0.6      |
| Cognitive Load               | 7.5 $\pm$ 0.5      |
| Social Support               | 8.4 $\pm$ 0.7      |
| Resilience                   | 8.4 $\pm$ 0.6      |






### gpt-4-1106-preview


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.4      |
| Emotional Stability          | 6.8 $\pm$ 0.3      |
| Problem-solving Skills       | 7.8 $\pm$ 0.2      |
| Creativity                   | 9.0 $\pm$ 0.1      |
| Interpersonal Relationships  | 6.8 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.0 $\pm$ 0.5      |
| Conflict Resolution          | 6.5 $\pm$ 0.5      |
| Work-related Stress          | 7.1 $\pm$ 0.9      |
| Adaptability                 | 7.8 $\pm$ 0.6      |
| Achievement Motivation       | 7.6 $\pm$ 0.4      |
| Fear of Failure              | 7.1 $\pm$ 0.4      |
| Need for Control             | 6.3 $\pm$ 0.3      |
| Cognitive Load               | 7.4 $\pm$ 0.4      |
| Social Support               | 7.0 $\pm$ 0.4      |
| Resilience                   | 7.8 $\pm$ 0.4      |






### meta-llamaMeta-Llama-3.1-8B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.2 $\pm$ 0.6      |
| Emotional Stability          | 6.3 $\pm$ 0.3      |
| Problem-solving Skills       | 8.2 $\pm$ 0.7      |
| Creativity                   | 9.7 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.1 $\pm$ 0.7      |
| Confidence and Self-efficacy | 5.7 $\pm$ 1.3      |
| Conflict Resolution          | 6.3 $\pm$ 0.5      |
| Work-related Stress          | 7.6 $\pm$ 0.4      |
| Adaptability                 | 7.7 $\pm$ 0.7      |
| Achievement Motivation       | 8.1 $\pm$ 0.7      |
| Fear of Failure              | 7.3 $\pm$ 0.6      |
| Need for Control             | 7.2 $\pm$ 1.2      |
| Cognitive Load               | 8.0 $\pm$ 0.7      |
| Social Support               | 5.7 $\pm$ 1.0      |
| Resilience                   | 8.0 $\pm$ 0.4      |






### meta-llamaMeta-Llama-3.1-70B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.8      |
| Emotional Stability          | 6.0 $\pm$ 0.5      |
| Problem-solving Skills       | 8.1 $\pm$ 0.4      |
| Creativity                   | 9.5 $\pm$ 0.0      |
| Interpersonal Relationships  | 6.4 $\pm$ 0.5      |
| Confidence and Self-efficacy | 6.4 $\pm$ 0.2      |
| Conflict Resolution          | 6.2 $\pm$ 0.8      |
| Work-related Stress          | 7.4 $\pm$ 0.4      |
| Adaptability                 | 7.7 $\pm$ 0.4      |
| Achievement Motivation       | 8.2 $\pm$ 0.6      |
| Fear of Failure              | 7.4 $\pm$ 0.4      |
| Need for Control             | 7.0 $\pm$ 0.4      |
| Cognitive Load               | 7.7 $\pm$ 0.3      |
| Social Support               | 6.0 $\pm$ 0.5      |
| Resilience                   | 7.8 $\pm$ 0.4      |






### meta-llamaMeta-Llama-3.1-405B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.1 $\pm$ 0.4      |
| Emotional Stability          | 5.8 $\pm$ 0.8      |
| Problem-solving Skills       | 8.2 $\pm$ 0.8      |
| Creativity                   | 9.5 $\pm$ 0.0      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.5 $\pm$ 0.4      |
| Conflict Resolution          | 6.5 $\pm$ 0.6      |
| Work-related Stress          | 7.8 $\pm$ 0.4      |
| Adaptability                 | 8.1 $\pm$ 0.4      |
| Achievement Motivation       | 8.0 $\pm$ 0.4      |
| Fear of Failure              | 7.2 $\pm$ 0.4      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 7.9 $\pm$ 0.5      |
| Social Support               | 6.6 $\pm$ 0.6      |
| Resilience                   | 7.9 $\pm$ 0.5      |






### open-mistral-nemo


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.8 $\pm$ 0.4      |
| Emotional Stability          | 7.4 $\pm$ 0.4      |
| Problem-solving Skills       | 8.5 $\pm$ 0.5      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.6      |
| Conflict Resolution          | 7.5 $\pm$ 0.4      |
| Work-related Stress          | 6.8 $\pm$ 0.2      |
| Adaptability                 | 8.5 $\pm$ 0.4      |
| Achievement Motivation       | 8.4 $\pm$ 0.2      |
| Fear of Failure              | 5.8 $\pm$ 0.6      |
| Need for Control             | 6.9 $\pm$ 0.4      |
| Cognitive Load               | 7.6 $\pm$ 0.6      |
| Social Support               | 7.1 $\pm$ 0.4      |
| Resilience                   | 8.1 $\pm$ 0.2      |






### mistral-large-2407


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.2 $\pm$ 0.8      |
| Emotional Stability          | 7.5 $\pm$ 0.9      |
| Problem-solving Skills       | 8.8 $\pm$ 0.6      |
| Creativity                   | 9.4 $\pm$ 0.3      |
| Interpersonal Relationships  | 7.6 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.8      |
| Conflict Resolution          | 8.0 $\pm$ 0.4      |
| Work-related Stress          | 6.8 $\pm$ 0.8      |
| Adaptability                 | 8.6 $\pm$ 0.6      |
| Achievement Motivation       | 8.6 $\pm$ 0.2      |
| Fear of Failure              | 5.9 $\pm$ 0.7      |
| Need for Control             | 6.9 $\pm$ 0.4      |
| Cognitive Load               | 7.5 $\pm$ 0.6      |
| Social Support               | 7.5 $\pm$ 0.5      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### open-mixtral-8x22b


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.2 $\pm$ 0.4      |
| Emotional Stability          | 7.8 $\pm$ 0.4      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.4 $\pm$ 0.4      |
| Interpersonal Relationships  | 8.4 $\pm$ 0.2      |
| Confidence and Self-efficacy | 8.4 $\pm$ 0.3      |
| Conflict Resolution          | 7.6 $\pm$ 0.4      |
| Work-related Stress          | 6.8 $\pm$ 0.2      |
| Adaptability                 | 8.8 $\pm$ 0.2      |
| Achievement Motivation       | 9.0 $\pm$ 0.4      |
| Fear of Failure              | 5.5 $\pm$ 1.0      |
| Need for Control             | 6.9 $\pm$ 0.4      |
| Cognitive Load               | 8.0 $\pm$ 0.4      |
| Social Support               | 8.2 $\pm$ 0.2      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### microsoftPhi-3-medium-4k-instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.5 $\pm$ 0.7      |
| Emotional Stability          | 8.2 $\pm$ 0.6      |
| Problem-solving Skills       | 9.2 $\pm$ 0.2      |
| Creativity                   | 9.6 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.4 $\pm$ 0.3      |
| Confidence and Self-efficacy | 8.1 $\pm$ 0.2      |
| Conflict Resolution          | 8.5 $\pm$ 0.3      |
| Work-related Stress          | 7.0 $\pm$ 0.4      |
| Adaptability                 | 9.2 $\pm$ 0.3      |
| Achievement Motivation       | 9.2 $\pm$ 0.2      |
| Fear of Failure              | 5.9 $\pm$ 0.8      |
| Need for Control             | 6.7 $\pm$ 0.3      |
| Cognitive Load               | 8.0 $\pm$ 0.4      |
| Social Support               | 8.4 $\pm$ 0.2      |
| Resilience                   | 9.0 $\pm$ 0.3      |






### googlegemma-2-9b-it


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.2 $\pm$ 0.6      |
| Emotional Stability          | 7.0 $\pm$ 0.5      |
| Problem-solving Skills       | 8.4 $\pm$ 0.4      |
| Creativity                   | 9.5 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.1 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.4 $\pm$ 0.7      |
| Conflict Resolution          | 7.4 $\pm$ 0.5      |
| Work-related Stress          | 7.3 $\pm$ 0.8      |
| Adaptability                 | 8.8 $\pm$ 0.2      |
| Achievement Motivation       | 8.4 $\pm$ 0.3      |
| Fear of Failure              | 7.0 $\pm$ 0.8      |
| Need for Control             | 6.7 $\pm$ 0.5      |
| Cognitive Load               | 7.9 $\pm$ 0.5      |
| Social Support               | 7.3 $\pm$ 0.2      |
| Resilience                   | 8.7 $\pm$ 0.2      |






### googlegemma-2-27b-it


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.6 $\pm$ 0.4      |
| Emotional Stability          | 4.9 $\pm$ 1.2      |
| Problem-solving Skills       | 7.0 $\pm$ 0.6      |
| Creativity                   | 8.6 $\pm$ 0.4      |
| Interpersonal Relationships  | 4.8 $\pm$ 0.8      |
| Confidence and Self-efficacy | 5.0 $\pm$ 1.2      |
| Conflict Resolution          | 4.9 $\pm$ 0.4      |
| Work-related Stress          | 8.0 $\pm$ 0.4      |
| Adaptability                 | 5.4 $\pm$ 1.0      |
| Achievement Motivation       | 6.8 $\pm$ 0.2      |
| Fear of Failure              | 8.4 $\pm$ 0.4      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 8.8 $\pm$ 0.4      |
| Social Support               | 3.8 $\pm$ 0.6      |
| Resilience                   | 5.8 $\pm$ 1.0      |






### gpt-4o-2024-08-06


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.1 $\pm$ 1.3      |
| Emotional Stability          | 7.6 $\pm$ 0.6      |
| Problem-solving Skills       | 8.7 $\pm$ 0.4      |
| Creativity                   | 9.8 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.5      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.9      |
| Conflict Resolution          | 7.7 $\pm$ 0.3      |
| Work-related Stress          | 6.1 $\pm$ 1.1      |
| Adaptability                 | 8.6 $\pm$ 0.4      |
| Achievement Motivation       | 8.0 $\pm$ 0.7      |
| Fear of Failure              | 5.6 $\pm$ 1.0      |
| Need for Control             | 6.5 $\pm$ 0.6      |
| Cognitive Load               | 7.3 $\pm$ 0.6      |
| Social Support               | 7.7 $\pm$ 0.7      |
| Resilience                   | 8.4 $\pm$ 0.4      |






### Gemini-1.5-Pro-Exp-0801


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.4 $\pm$ 0.2      |
| Emotional Stability          | 6.6 $\pm$ 0.4      |
| Problem-solving Skills       | 8.8 $\pm$ 0.4      |
| Creativity                   | 9.8 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.6 $\pm$ 0.5      |
| Confidence and Self-efficacy | 6.5 $\pm$ 0.7      |
| Conflict Resolution          | 7.4 $\pm$ 0.4      |
| Work-related Stress          | 7.6 $\pm$ 0.4      |
| Adaptability                 | 8.4 $\pm$ 0.5      |
| Achievement Motivation       | 8.8 $\pm$ 0.2      |
| Fear of Failure              | 7.6 $\pm$ 1.0      |
| Need for Control             | 6.6 $\pm$ 0.5      |
| Cognitive Load               | 7.9 $\pm$ 0.2      |
| Social Support               | 7.0 $\pm$ 0.6      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### googlegemma-2-2b-it


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.1 $\pm$ 0.2      |
| Emotional Stability          | 6.0 $\pm$ 0.6      |
| Problem-solving Skills       | 8.0 $\pm$ 0.6      |
| Creativity                   | 9.1 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.1 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.9 $\pm$ 0.4      |
| Conflict Resolution          | 6.5 $\pm$ 0.4      |
| Work-related Stress          | 7.8 $\pm$ 0.2      |
| Adaptability                 | 8.4 $\pm$ 0.2      |
| Achievement Motivation       | 8.1 $\pm$ 0.7      |
| Fear of Failure              | 7.4 $\pm$ 0.4      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 8.2 $\pm$ 0.4      |
| Social Support               | 6.5 $\pm$ 0.7      |
| Resilience                   | 8.1 $\pm$ 0.4      |






### phi3.53.8b-mini-instruct-fp16


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.4      |
| Emotional Stability          | 7.6 $\pm$ 0.7      |
| Problem-solving Skills       | 9.2 $\pm$ 0.2      |
| Creativity                   | 9.4 $\pm$ 0.5      |
| Interpersonal Relationships  | 7.9 $\pm$ 0.6      |
| Confidence and Self-efficacy | 8.2 $\pm$ 0.4      |
| Conflict Resolution          | 7.6 $\pm$ 0.4      |
| Work-related Stress          | 7.3 $\pm$ 0.6      |
| Adaptability                 | 8.8 $\pm$ 0.4      |
| Achievement Motivation       | 8.8 $\pm$ 0.4      |
| Fear of Failure              | 6.7 $\pm$ 0.5      |
| Need for Control             | 6.9 $\pm$ 0.2      |
| Cognitive Load               | 8.0 $\pm$ 0.4      |
| Social Support               | 8.0 $\pm$ 0.6      |
| Resilience                   | 8.9 $\pm$ 0.5      |






### gpt-3.5-turbo


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.5 $\pm$ 0.4      |
| Emotional Stability          | 7.4 $\pm$ 0.6      |
| Problem-solving Skills       | 8.7 $\pm$ 0.5      |
| Creativity                   | 9.1 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.5      |
| Confidence and Self-efficacy | 8.4 $\pm$ 0.3      |
| Conflict Resolution          | 7.8 $\pm$ 0.6      |
| Work-related Stress          | 7.6 $\pm$ 0.4      |
| Adaptability                 | 8.5 $\pm$ 0.4      |
| Achievement Motivation       | 8.8 $\pm$ 0.4      |
| Fear of Failure              | 6.7 $\pm$ 0.2      |
| Need for Control             | 6.7 $\pm$ 0.5      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 8.2 $\pm$ 0.2      |
| Resilience                   | 9.0 $\pm$ 0.3      |






### gpt-4-0613


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.9 $\pm$ 0.5      |
| Emotional Stability          | 6.6 $\pm$ 0.4      |
| Problem-solving Skills       | 9.0 $\pm$ 0.4      |
| Creativity                   | 9.5 $\pm$ 0.5      |
| Interpersonal Relationships  | 7.4 $\pm$ 0.2      |
| Confidence and Self-efficacy | 8.2 $\pm$ 0.2      |
| Conflict Resolution          | 7.6 $\pm$ 0.2      |
| Work-related Stress          | 7.4 $\pm$ 0.2      |
| Adaptability                 | 8.9 $\pm$ 0.4      |
| Achievement Motivation       | 8.6 $\pm$ 0.6      |
| Fear of Failure              | 5.8 $\pm$ 1.6      |
| Need for Control             | 6.8 $\pm$ 0.2      |
| Cognitive Load               | 8.0 $\pm$ 0.4      |
| Social Support               | 7.1 $\pm$ 0.4      |
| Resilience                   | 8.8 $\pm$ 0.2      |






### Gemini-1.5-Pro-Exp-0827


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.8 $\pm$ 0.4      |
| Emotional Stability          | 5.9 $\pm$ 0.8      |
| Problem-solving Skills       | 8.0 $\pm$ 0.4      |
| Creativity                   | 9.5 $\pm$ 0.4      |
| Interpersonal Relationships  | 6.8 $\pm$ 0.8      |
| Confidence and Self-efficacy | 5.9 $\pm$ 0.7      |
| Conflict Resolution          | 6.0 $\pm$ 1.2      |
| Work-related Stress          | 8.2 $\pm$ 0.2      |
| Adaptability                 | 7.8 $\pm$ 0.6      |
| Achievement Motivation       | 8.1 $\pm$ 0.6      |
| Fear of Failure              | 6.9 $\pm$ 0.9      |
| Need for Control             | 6.2 $\pm$ 0.8      |
| Cognitive Load               | 8.0 $\pm$ 0.6      |
| Social Support               | 6.6 $\pm$ 0.4      |
| Resilience                   | 7.5 $\pm$ 0.6      |






### o1-mini


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.9 $\pm$ 1.3      |
| Emotional Stability          | 7.5 $\pm$ 0.4      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.5 $\pm$ 0.4      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.1 $\pm$ 0.4      |
| Conflict Resolution          | 7.9 $\pm$ 0.5      |
| Work-related Stress          | 7.1 $\pm$ 0.8      |
| Adaptability                 | 8.9 $\pm$ 0.2      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 6.1 $\pm$ 0.8      |
| Need for Control             | 6.6 $\pm$ 0.6      |
| Cognitive Load               | 7.8 $\pm$ 0.6      |
| Social Support               | 8.0 $\pm$ 0.4      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### gemini-1.5-flash-002


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.4      |
| Emotional Stability          | 7.1 $\pm$ 0.7      |
| Problem-solving Skills       | 8.8 $\pm$ 0.5      |
| Creativity                   | 9.8 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.8 $\pm$ 1.2      |
| Conflict Resolution          | 7.4 $\pm$ 1.0      |
| Work-related Stress          | 7.7 $\pm$ 0.3      |
| Adaptability                 | 8.0 $\pm$ 0.8      |
| Achievement Motivation       | 8.6 $\pm$ 0.6      |
| Fear of Failure              | 6.8 $\pm$ 0.2      |
| Need for Control             | 6.6 $\pm$ 0.6      |
| Cognitive Load               | 8.3 $\pm$ 0.5      |
| Social Support               | 6.8 $\pm$ 1.0      |
| Resilience                   | 8.4 $\pm$ 0.4      |






### gemini-1.5-flash-8b


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.6 $\pm$ 0.7      |
| Emotional Stability          | 6.5 $\pm$ 0.5      |
| Problem-solving Skills       | 8.8 $\pm$ 0.2      |
| Creativity                   | 9.7 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.9 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.2      |
| Conflict Resolution          | 7.4 $\pm$ 0.3      |
| Work-related Stress          | 7.9 $\pm$ 0.8      |
| Adaptability                 | 8.1 $\pm$ 0.2      |
| Achievement Motivation       | 8.7 $\pm$ 0.2      |
| Fear of Failure              | 7.1 $\pm$ 0.6      |
| Need for Control             | 7.4 $\pm$ 0.8      |
| Cognitive Load               | 8.4 $\pm$ 0.5      |
| Social Support               | 6.6 $\pm$ 0.9      |
| Resilience                   | 8.6 $\pm$ 0.3      |






### gemini-exp-1114


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.2 $\pm$ 0.5      |
| Emotional Stability          | 6.9 $\pm$ 0.5      |
| Problem-solving Skills       | 8.0 $\pm$ 0.6      |
| Creativity                   | 9.0 $\pm$ 0.0      |
| Interpersonal Relationships  | 6.5 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.8 $\pm$ 0.4      |
| Conflict Resolution          | 7.0 $\pm$ 0.4      |
| Work-related Stress          | 8.2 $\pm$ 0.3      |
| Adaptability                 | 8.1 $\pm$ 0.4      |
| Achievement Motivation       | 8.8 $\pm$ 0.2      |
| Fear of Failure              | 7.2 $\pm$ 0.6      |
| Need for Control             | 7.0 $\pm$ 0.4      |
| Cognitive Load               | 8.3 $\pm$ 0.4      |
| Social Support               | 6.4 $\pm$ 0.6      |
| Resilience                   | 8.3 $\pm$ 0.5      |






### o1-preview-2024-09-12


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.0 $\pm$ 0.6      |
| Emotional Stability          | 7.8 $\pm$ 0.4      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.9 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.9 $\pm$ 0.4      |
| Conflict Resolution          | 7.5 $\pm$ 0.5      |
| Work-related Stress          | 6.8 $\pm$ 1.0      |
| Adaptability                 | 8.8 $\pm$ 0.2      |
| Achievement Motivation       | 8.2 $\pm$ 0.2      |
| Fear of Failure              | 6.1 $\pm$ 0.6      |
| Need for Control             | 6.5 $\pm$ 0.4      |
| Cognitive Load               | 7.6 $\pm$ 0.5      |
| Social Support               | 7.9 $\pm$ 0.5      |
| Resilience                   | 8.8 $\pm$ 0.2      |






### ministral-3b-2410


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.5 $\pm$ 0.4      |
| Emotional Stability          | 7.5 $\pm$ 0.6      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.2 $\pm$ 0.6      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.6      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.4      |
| Conflict Resolution          | 7.6 $\pm$ 0.7      |
| Work-related Stress          | 7.1 $\pm$ 0.2      |
| Adaptability                 | 8.7 $\pm$ 0.2      |
| Achievement Motivation       | 8.4 $\pm$ 0.4      |
| Fear of Failure              | 6.4 $\pm$ 0.2      |
| Need for Control             | 7.2 $\pm$ 0.4      |
| Cognitive Load               | 7.9 $\pm$ 0.3      |
| Social Support               | 7.6 $\pm$ 0.6      |
| Resilience                   | 8.4 $\pm$ 0.4      |






### ministral-8b-2410


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.1 $\pm$ 0.7      |
| Emotional Stability          | 7.1 $\pm$ 0.6      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.1 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.1 $\pm$ 0.7      |
| Confidence and Self-efficacy | 7.4 $\pm$ 0.2      |
| Conflict Resolution          | 7.8 $\pm$ 0.6      |
| Work-related Stress          | 7.6 $\pm$ 0.7      |
| Adaptability                 | 8.6 $\pm$ 0.4      |
| Achievement Motivation       | 8.4 $\pm$ 0.2      |
| Fear of Failure              | 6.8 $\pm$ 0.8      |
| Need for Control             | 6.6 $\pm$ 0.2      |
| Cognitive Load               | 7.8 $\pm$ 0.4      |
| Social Support               | 7.4 $\pm$ 1.0      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### meta-llamaLlama-3.2-1B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.4 $\pm$ 0.7      |
| Emotional Stability          | 6.1 $\pm$ 0.7      |
| Problem-solving Skills       | 7.8 $\pm$ 1.0      |
| Creativity                   | 9.0 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.8 $\pm$ 1.0      |
| Conflict Resolution          | 5.8 $\pm$ 0.6      |
| Work-related Stress          | 7.5 $\pm$ 0.4      |
| Adaptability                 | 7.5 $\pm$ 0.8      |
| Achievement Motivation       | 8.1 $\pm$ 0.2      |
| Fear of Failure              | 6.5 $\pm$ 0.6      |
| Need for Control             | 6.5 $\pm$ 0.6      |
| Cognitive Load               | 6.9 $\pm$ 0.5      |
| Social Support               | 6.9 $\pm$ 0.6      |
| Resilience                   | 7.6 $\pm$ 0.7      |






### meta-llamaLlama-3.2-3B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.2      |
| Emotional Stability          | 6.6 $\pm$ 0.2      |
| Problem-solving Skills       | 8.4 $\pm$ 0.2      |
| Creativity                   | 9.0 $\pm$ 0.4      |
| Interpersonal Relationships  | 6.9 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.0 $\pm$ 0.4      |
| Conflict Resolution          | 6.7 $\pm$ 0.6      |
| Work-related Stress          | 7.9 $\pm$ 0.2      |
| Adaptability                 | 8.4 $\pm$ 0.4      |
| Achievement Motivation       | 8.3 $\pm$ 0.5      |
| Fear of Failure              | 7.2 $\pm$ 0.2      |
| Need for Control             | 7.0 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.5      |
| Social Support               | 6.9 $\pm$ 0.6      |
| Resilience                   | 8.2 $\pm$ 0.2      |






### nvidiaLlama-3.1-Nemotron-70B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.1 $\pm$ 0.4      |
| Emotional Stability          | 6.6 $\pm$ 0.2      |
| Problem-solving Skills       | 9.0 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.3      |
| Interpersonal Relationships  | 7.7 $\pm$ 0.3      |
| Confidence and Self-efficacy | 7.3 $\pm$ 0.3      |
| Conflict Resolution          | 7.3 $\pm$ 0.9      |
| Work-related Stress          | 7.4 $\pm$ 0.8      |
| Adaptability                 | 8.5 $\pm$ 0.4      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 6.9 $\pm$ 0.2      |
| Need for Control             | 7.4 $\pm$ 0.6      |
| Cognitive Load               | 7.7 $\pm$ 0.3      |
| Social Support               | 7.5 $\pm$ 0.5      |
| Resilience                   | 8.5 $\pm$ 0.0      |






### open-mistral-7b


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.9 $\pm$ 0.6      |
| Emotional Stability          | 8.1 $\pm$ 0.2      |
| Problem-solving Skills       | 8.9 $\pm$ 0.5      |
| Creativity                   | 9.0 $\pm$ 0.4      |
| Interpersonal Relationships  | 8.1 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.4 $\pm$ 0.2      |
| Conflict Resolution          | 7.6 $\pm$ 0.4      |
| Work-related Stress          | 6.9 $\pm$ 0.2      |
| Adaptability                 | 8.8 $\pm$ 0.2      |
| Achievement Motivation       | 8.9 $\pm$ 0.2      |
| Fear of Failure              | 6.0 $\pm$ 0.4      |
| Need for Control             | 6.5 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.2      |
| Social Support               | 8.0 $\pm$ 0.6      |
| Resilience                   | 8.6 $\pm$ 0.2      |






### chatgpt-4o-latest-2024-11-20


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.6      |
| Emotional Stability          | 6.8 $\pm$ 0.2      |
| Problem-solving Skills       | 8.6 $\pm$ 0.2      |
| Creativity                   | 9.4 $\pm$ 0.4      |
| Interpersonal Relationships  | 6.6 $\pm$ 0.5      |
| Confidence and Self-efficacy | 7.0 $\pm$ 0.6      |
| Conflict Resolution          | 6.8 $\pm$ 0.2      |
| Work-related Stress          | 8.0 $\pm$ 0.4      |
| Adaptability                 | 8.5 $\pm$ 0.7      |
| Achievement Motivation       | 8.0 $\pm$ 0.4      |
| Fear of Failure              | 6.8 $\pm$ 0.8      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.4      |
| Social Support               | 6.2 $\pm$ 0.6      |
| Resilience                   | 8.1 $\pm$ 0.2      |






### qwq32b-preview-q4_K_M


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.0 $\pm$ 1.5      |
| Emotional Stability          | 6.6 $\pm$ 1.1      |
| Problem-solving Skills       | 8.2 $\pm$ 1.0      |
| Creativity                   | 7.8 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.9 $\pm$ 1.0      |
| Confidence and Self-efficacy | 7.0 $\pm$ 0.7      |
| Conflict Resolution          | 6.6 $\pm$ 0.7      |
| Work-related Stress          | 6.9 $\pm$ 1.0      |
| Adaptability                 | 8.0 $\pm$ 0.6      |
| Achievement Motivation       | 8.1 $\pm$ 0.6      |
| Fear of Failure              | 6.1 $\pm$ 1.3      |
| Need for Control             | 6.5 $\pm$ 1.4      |
| Cognitive Load               | 7.0 $\pm$ 0.8      |
| Social Support               | 6.8 $\pm$ 1.1      |
| Resilience                   | 7.9 $\pm$ 0.7      |






### DeepSeek-R1-Lite-Preview


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.8      |
| Emotional Stability          | 6.6 $\pm$ 0.5      |
| Problem-solving Skills       | 8.2 $\pm$ 0.2      |
| Creativity                   | 8.5 $\pm$ 0.6      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.9 $\pm$ 0.7      |
| Conflict Resolution          | 6.9 $\pm$ 0.2      |
| Work-related Stress          | 7.5 $\pm$ 0.6      |
| Adaptability                 | 8.4 $\pm$ 0.4      |
| Achievement Motivation       | 8.4 $\pm$ 0.2      |
| Fear of Failure              | 6.4 $\pm$ 0.4      |
| Need for Control             | 7.0 $\pm$ 0.4      |
| Cognitive Load               | 7.5 $\pm$ 0.4      |
| Social Support               | 7.0 $\pm$ 0.0      |
| Resilience                   | 8.4 $\pm$ 0.2      |






### gemini-2.0-flash-exp


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.4      |
| Emotional Stability          | 6.7 $\pm$ 0.9      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.1 $\pm$ 0.6      |
| Conflict Resolution          | 7.2 $\pm$ 0.8      |
| Work-related Stress          | 7.6 $\pm$ 0.3      |
| Adaptability                 | 8.4 $\pm$ 0.3      |
| Achievement Motivation       | 8.0 $\pm$ 0.4      |
| Fear of Failure              | 6.4 $\pm$ 0.6      |
| Need for Control             | 6.5 $\pm$ 0.4      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 7.2 $\pm$ 0.6      |
| Resilience                   | 8.4 $\pm$ 0.2      |






### gemini-exp-1206


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.9 $\pm$ 0.4      |
| Emotional Stability          | 6.9 $\pm$ 0.7      |
| Problem-solving Skills       | 8.6 $\pm$ 0.6      |
| Creativity                   | 9.9 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.9 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.8      |
| Conflict Resolution          | 7.0 $\pm$ 0.8      |
| Work-related Stress          | 7.4 $\pm$ 0.6      |
| Adaptability                 | 8.8 $\pm$ 0.8      |
| Achievement Motivation       | 8.1 $\pm$ 0.6      |
| Fear of Failure              | 6.5 $\pm$ 0.8      |
| Need for Control             | 7.0 $\pm$ 0.7      |
| Cognitive Load               | 7.5 $\pm$ 0.0      |
| Social Support               | 6.6 $\pm$ 0.5      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### grok-2-1212


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.5 $\pm$ 0.4      |
| Emotional Stability          | 7.9 $\pm$ 0.2      |
| Problem-solving Skills       | 9.0 $\pm$ 0.0      |
| Creativity                   | 8.8 $\pm$ 0.4      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.3 $\pm$ 0.2      |
| Conflict Resolution          | 7.7 $\pm$ 0.4      |
| Work-related Stress          | 7.5 $\pm$ 0.5      |
| Adaptability                 | 8.7 $\pm$ 0.2      |
| Achievement Motivation       | 9.0 $\pm$ 0.1      |
| Fear of Failure              | 6.6 $\pm$ 0.2      |
| Need for Control             | 7.1 $\pm$ 0.5      |
| Cognitive Load               | 8.1 $\pm$ 0.5      |
| Social Support               | 8.0 $\pm$ 0.4      |
| Resilience                   | 8.7 $\pm$ 0.2      |






### meta-llamaLlama-3.3-70B-Instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.5 $\pm$ 0.4      |
| Emotional Stability          | 5.7 $\pm$ 0.4      |
| Problem-solving Skills       | 8.3 $\pm$ 0.6      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.3 $\pm$ 0.5      |
| Conflict Resolution          | 6.9 $\pm$ 0.2      |
| Work-related Stress          | 8.0 $\pm$ 0.4      |
| Adaptability                 | 8.2 $\pm$ 0.5      |
| Achievement Motivation       | 8.2 $\pm$ 0.7      |
| Fear of Failure              | 7.9 $\pm$ 0.4      |
| Need for Control             | 6.5 $\pm$ 0.6      |
| Cognitive Load               | 7.9 $\pm$ 0.7      |
| Social Support               | 7.0 $\pm$ 0.8      |
| Resilience                   | 8.2 $\pm$ 0.2      |






### mistral-large-2411


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.4 $\pm$ 1.1      |
| Emotional Stability          | 7.2 $\pm$ 0.5      |
| Problem-solving Skills       | 8.7 $\pm$ 0.4      |
| Creativity                   | 9.6 $\pm$ 0.3      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.6      |
| Confidence and Self-efficacy | 7.9 $\pm$ 0.3      |
| Conflict Resolution          | 7.2 $\pm$ 0.7      |
| Work-related Stress          | 7.0 $\pm$ 0.6      |
| Adaptability                 | 8.8 $\pm$ 0.4      |
| Achievement Motivation       | 8.3 $\pm$ 0.3      |
| Fear of Failure              | 6.2 $\pm$ 1.0      |
| Need for Control             | 6.8 $\pm$ 0.6      |
| Cognitive Load               | 7.8 $\pm$ 0.4      |
| Social Support               | 7.2 $\pm$ 0.5      |
| Resilience                   | 8.3 $\pm$ 0.4      |






### mistral-small-2409


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.5 $\pm$ 1.1      |
| Emotional Stability          | 7.1 $\pm$ 0.4      |
| Problem-solving Skills       | 8.4 $\pm$ 0.2      |
| Creativity                   | 9.0 $\pm$ 0.0      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.6      |
| Confidence and Self-efficacy | 7.2 $\pm$ 0.6      |
| Conflict Resolution          | 7.5 $\pm$ 0.4      |
| Work-related Stress          | 6.6 $\pm$ 0.4      |
| Adaptability                 | 8.4 $\pm$ 0.2      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 6.0 $\pm$ 0.6      |
| Need for Control             | 6.8 $\pm$ 0.6      |
| Cognitive Load               | 7.2 $\pm$ 0.2      |
| Social Support               | 7.1 $\pm$ 0.7      |
| Resilience                   | 7.9 $\pm$ 0.2      |






### o1-2024-12-05


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.2 $\pm$ 0.6      |
| Emotional Stability          | 6.7 $\pm$ 0.5      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.3 $\pm$ 0.6      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.8      |
| Confidence and Self-efficacy | 7.2 $\pm$ 0.5      |
| Conflict Resolution          | 7.6 $\pm$ 0.2      |
| Work-related Stress          | 7.6 $\pm$ 0.9      |
| Adaptability                 | 8.8 $\pm$ 0.4      |
| Achievement Motivation       | 8.3 $\pm$ 0.4      |
| Fear of Failure              | 7.0 $\pm$ 0.4      |
| Need for Control             | 7.0 $\pm$ 0.3      |
| Cognitive Load               | 7.9 $\pm$ 0.5      |
| Social Support               | 6.8 $\pm$ 0.8      |
| Resilience                   | 8.4 $\pm$ 0.2      |






### o1-pro-2024-12-05


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.4      |
| Emotional Stability          | 6.6 $\pm$ 0.2      |
| Problem-solving Skills       | 8.8 $\pm$ 0.2      |
| Creativity                   | 9.4 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.4 $\pm$ 0.4      |
| Conflict Resolution          | 7.0 $\pm$ 0.8      |
| Work-related Stress          | 7.6 $\pm$ 0.2      |
| Adaptability                 | 8.8 $\pm$ 0.6      |
| Achievement Motivation       | 8.0 $\pm$ 0.4      |
| Fear of Failure              | 6.4 $\pm$ 0.6      |
| Need for Control             | 6.5 $\pm$ 0.4      |
| Cognitive Load               | 8.1 $\pm$ 0.2      |
| Social Support               | 6.6 $\pm$ 0.4      |
| Resilience                   | 8.2 $\pm$ 0.6      |






### open-mixtral-8x7b


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.6 $\pm$ 0.4      |
| Emotional Stability          | 8.0 $\pm$ 0.4      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.1 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.1 $\pm$ 0.4      |
| Conflict Resolution          | 7.5 $\pm$ 0.0      |
| Work-related Stress          | 6.9 $\pm$ 0.2      |
| Adaptability                 | 8.8 $\pm$ 0.2      |
| Achievement Motivation       | 8.2 $\pm$ 0.2      |
| Fear of Failure              | 5.6 $\pm$ 0.7      |
| Need for Control             | 6.5 $\pm$ 0.6      |
| Cognitive Load               | 7.1 $\pm$ 0.5      |
| Social Support               | 7.6 $\pm$ 0.5      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### gpt-4o-mini-2024-11-05


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.2      |
| Emotional Stability          | 6.4 $\pm$ 0.2      |
| Problem-solving Skills       | 8.4 $\pm$ 0.2      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.0 $\pm$ 0.6      |
| Confidence and Self-efficacy | 6.4 $\pm$ 0.4      |
| Conflict Resolution          | 7.0 $\pm$ 0.4      |
| Work-related Stress          | 7.2 $\pm$ 0.3      |
| Adaptability                 | 8.1 $\pm$ 0.1      |
| Achievement Motivation       | 8.0 $\pm$ 0.0      |
| Fear of Failure              | 7.1 $\pm$ 0.2      |
| Need for Control             | 6.8 $\pm$ 0.6      |
| Cognitive Load               | 8.0 $\pm$ 0.5      |
| Social Support               | 6.4 $\pm$ 0.9      |
| Resilience                   | 7.5 $\pm$ 0.4      |






### o1-2024-12-17


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.7      |
| Emotional Stability          | 6.8 $\pm$ 0.4      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.4 $\pm$ 0.7      |
| Confidence and Self-efficacy | 7.0 $\pm$ 0.0      |
| Conflict Resolution          | 7.3 $\pm$ 0.8      |
| Work-related Stress          | 7.8 $\pm$ 0.2      |
| Adaptability                 | 8.8 $\pm$ 0.3      |
| Achievement Motivation       | 8.2 $\pm$ 0.2      |
| Fear of Failure              | 7.2 $\pm$ 0.6      |
| Need for Control             | 6.8 $\pm$ 0.6      |
| Cognitive Load               | 7.9 $\pm$ 0.5      |
| Social Support               | 6.0 $\pm$ 0.7      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### o1-pro-2024-12-17


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.0 $\pm$ 0.5      |
| Emotional Stability          | 6.8 $\pm$ 0.2      |
| Problem-solving Skills       | 8.5 $\pm$ 0.5      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.8      |
| Confidence and Self-efficacy | 7.2 $\pm$ 1.0      |
| Conflict Resolution          | 6.9 $\pm$ 0.6      |
| Work-related Stress          | 7.0 $\pm$ 1.2      |
| Adaptability                 | 8.0 $\pm$ 0.6      |
| Achievement Motivation       | 7.9 $\pm$ 0.9      |
| Fear of Failure              | 7.1 $\pm$ 1.0      |
| Need for Control             | 7.0 $\pm$ 0.9      |
| Cognitive Load               | 8.4 $\pm$ 0.4      |
| Social Support               | 6.2 $\pm$ 0.9      |
| Resilience                   | 8.3 $\pm$ 0.8      |






### o3-mini-20250131-HIGH


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.4 $\pm$ 0.7      |
| Emotional Stability          | 7.2 $\pm$ 0.9      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.6 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.5 $\pm$ 0.5      |
| Confidence and Self-efficacy | 7.9 $\pm$ 0.4      |
| Conflict Resolution          | 7.6 $\pm$ 0.4      |
| Work-related Stress          | 7.0 $\pm$ 0.7      |
| Adaptability                 | 8.7 $\pm$ 0.2      |
| Achievement Motivation       | 8.2 $\pm$ 0.2      |
| Fear of Failure              | 5.9 $\pm$ 0.6      |
| Need for Control             | 6.1 $\pm$ 0.6      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 7.4 $\pm$ 0.8      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### deepseek-aiDeepSeek-R1-Distill-Llama-70B


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.2 $\pm$ 0.6      |
| Emotional Stability          | 7.0 $\pm$ 0.4      |
| Problem-solving Skills       | 8.8 $\pm$ 0.2      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.8      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.5      |
| Conflict Resolution          | 7.4 $\pm$ 0.3      |
| Work-related Stress          | 7.6 $\pm$ 1.1      |
| Adaptability                 | 8.6 $\pm$ 0.2      |
| Achievement Motivation       | 8.2 $\pm$ 0.6      |
| Fear of Failure              | 6.9 $\pm$ 0.2      |
| Need for Control             | 6.9 $\pm$ 0.6      |
| Cognitive Load               | 7.8 $\pm$ 0.4      |
| Social Support               | 7.6 $\pm$ 0.9      |
| Resilience                   | 8.6 $\pm$ 0.2      |






### microsoftphi-4


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.3 $\pm$ 0.5      |
| Emotional Stability          | 8.0 $\pm$ 0.1      |
| Problem-solving Skills       | 9.0 $\pm$ 0.4      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.2 $\pm$ 0.4      |
| Confidence and Self-efficacy | 8.1 $\pm$ 0.7      |
| Conflict Resolution          | 8.1 $\pm$ 0.2      |
| Work-related Stress          | 6.8 $\pm$ 0.8      |
| Adaptability                 | 9.1 $\pm$ 0.1      |
| Achievement Motivation       | 8.6 $\pm$ 0.1      |
| Fear of Failure              | 5.4 $\pm$ 0.9      |
| Need for Control             | 7.0 $\pm$ 0.6      |
| Cognitive Load               | 7.4 $\pm$ 0.4      |
| Social Support               | 8.0 $\pm$ 0.4      |
| Resilience                   | 9.1 $\pm$ 0.2      |






### gemini-2.0-flash-thinking-exp-01-21


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.4 $\pm$ 0.4      |
| Emotional Stability          | 5.8 $\pm$ 1.4      |
| Problem-solving Skills       | 7.6 $\pm$ 0.7      |
| Creativity                   | 9.3 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.6 $\pm$ 1.0      |
| Confidence and Self-efficacy | 6.4 $\pm$ 0.4      |
| Conflict Resolution          | 6.4 $\pm$ 0.7      |
| Work-related Stress          | 7.9 $\pm$ 0.3      |
| Adaptability                 | 8.0 $\pm$ 0.7      |
| Achievement Motivation       | 7.3 $\pm$ 0.7      |
| Fear of Failure              | 7.2 $\pm$ 0.5      |
| Need for Control             | 6.5 $\pm$ 0.6      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 6.4 $\pm$ 0.6      |
| Resilience                   | 8.0 $\pm$ 0.6      |






### mistral-small-2501


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.7 $\pm$ 1.0      |
| Emotional Stability          | 7.4 $\pm$ 0.8      |
| Problem-solving Skills       | 8.7 $\pm$ 0.7      |
| Creativity                   | 9.2 $\pm$ 0.7      |
| Interpersonal Relationships  | 7.4 $\pm$ 0.5      |
| Confidence and Self-efficacy | 7.4 $\pm$ 1.0      |
| Conflict Resolution          | 7.5 $\pm$ 0.4      |
| Work-related Stress          | 6.6 $\pm$ 1.1      |
| Adaptability                 | 8.4 $\pm$ 0.6      |
| Achievement Motivation       | 8.0 $\pm$ 0.7      |
| Fear of Failure              | 6.8 $\pm$ 0.6      |
| Need for Control             | 6.8 $\pm$ 0.6      |
| Cognitive Load               | 7.3 $\pm$ 0.7      |
| Social Support               | 7.3 $\pm$ 0.6      |
| Resilience                   | 8.2 $\pm$ 0.7      |






### deepseek-aiDeepSeek-R1-Zero


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.2      |
| Emotional Stability          | 7.1 $\pm$ 0.6      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 8.6 $\pm$ 0.5      |
| Interpersonal Relationships  | 7.4 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.5      |
| Conflict Resolution          | 7.0 $\pm$ 0.4      |
| Work-related Stress          | 7.5 $\pm$ 0.0      |
| Adaptability                 | 8.5 $\pm$ 0.4      |
| Achievement Motivation       | 8.6 $\pm$ 0.2      |
| Fear of Failure              | 6.6 $\pm$ 0.2      |
| Need for Control             | 6.9 $\pm$ 0.8      |
| Cognitive Load               | 7.9 $\pm$ 0.2      |
| Social Support               | 7.1 $\pm$ 0.9      |
| Resilience                   | 8.5 $\pm$ 0.4      |






### deepseek-aiDeepSeek-V3


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.9 $\pm$ 0.6      |
| Emotional Stability          | 6.6 $\pm$ 0.2      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.4 $\pm$ 0.8      |
| Conflict Resolution          | 7.2 $\pm$ 0.2      |
| Work-related Stress          | 7.5 $\pm$ 0.9      |
| Adaptability                 | 8.5 $\pm$ 0.0      |
| Achievement Motivation       | 8.1 $\pm$ 0.5      |
| Fear of Failure              | 6.5 $\pm$ 0.0      |
| Need for Control             | 6.9 $\pm$ 0.5      |
| Cognitive Load               | 7.9 $\pm$ 0.5      |
| Social Support               | 6.9 $\pm$ 0.5      |
| Resilience                   | 8.0 $\pm$ 0.4      |






### deepseek-aiDeepSeek-R1


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.4 $\pm$ 0.2      |
| Emotional Stability          | 7.1 $\pm$ 0.2      |
| Problem-solving Skills       | 9.0 $\pm$ 0.0      |
| Creativity                   | 9.5 $\pm$ 0.0      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.5      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.6      |
| Conflict Resolution          | 7.3 $\pm$ 0.4      |
| Work-related Stress          | 8.0 $\pm$ 0.4      |
| Adaptability                 | 8.4 $\pm$ 0.3      |
| Achievement Motivation       | 8.4 $\pm$ 0.3      |
| Fear of Failure              | 7.4 $\pm$ 0.3      |
| Need for Control             | 7.5 $\pm$ 0.5      |
| Cognitive Load               | 8.2 $\pm$ 0.2      |
| Social Support               | 6.8 $\pm$ 0.5      |
| Resilience                   | 8.7 $\pm$ 0.3      |






### gemini-2.0-flash-lite-preview-02-05


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.1 $\pm$ 0.6      |
| Emotional Stability          | 6.2 $\pm$ 0.8      |
| Problem-solving Skills       | 8.5 $\pm$ 0.5      |
| Creativity                   | 9.5 $\pm$ 0.0      |
| Interpersonal Relationships  | 6.6 $\pm$ 0.5      |
| Confidence and Self-efficacy | 6.1 $\pm$ 0.7      |
| Conflict Resolution          | 6.0 $\pm$ 1.3      |
| Work-related Stress          | 8.1 $\pm$ 0.6      |
| Adaptability                 | 8.4 $\pm$ 0.4      |
| Achievement Motivation       | 7.4 $\pm$ 0.5      |
| Fear of Failure              | 7.5 $\pm$ 0.4      |
| Need for Control             | 6.4 $\pm$ 0.8      |
| Cognitive Load               | 8.1 $\pm$ 0.2      |
| Social Support               | 6.1 $\pm$ 0.5      |
| Resilience                   | 7.6 $\pm$ 0.9      |






### chatgpt-4o-latest-2025-01-29


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 8.1 $\pm$ 0.4      |
| Emotional Stability          | 6.2 $\pm$ 0.4      |
| Problem-solving Skills       | 7.8 $\pm$ 0.2      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.4 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.2 $\pm$ 0.6      |
| Conflict Resolution          | 6.4 $\pm$ 0.4      |
| Work-related Stress          | 7.8 $\pm$ 0.6      |
| Adaptability                 | 8.0 $\pm$ 0.4      |
| Achievement Motivation       | 7.4 $\pm$ 0.4      |
| Fear of Failure              | 7.5 $\pm$ 0.4      |
| Need for Control             | 7.1 $\pm$ 0.4      |
| Cognitive Load               | 8.0 $\pm$ 0.7      |
| Social Support               | 6.2 $\pm$ 0.4      |
| Resilience                   | 7.5 $\pm$ 0.6      |






### qwen-turbo-2024-11-01


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.4 $\pm$ 0.7      |
| Emotional Stability          | 7.5 $\pm$ 0.4      |
| Problem-solving Skills       | 9.1 $\pm$ 0.2      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.5 $\pm$ 0.6      |
| Conflict Resolution          | 7.9 $\pm$ 0.4      |
| Work-related Stress          | 6.8 $\pm$ 0.2      |
| Adaptability                 | 8.6 $\pm$ 0.2      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 5.6 $\pm$ 0.5      |
| Need for Control             | 6.9 $\pm$ 0.4      |
| Cognitive Load               | 7.5 $\pm$ 0.5      |
| Social Support               | 7.8 $\pm$ 0.2      |
| Resilience                   | 8.8 $\pm$ 0.4      |






### qwen-plus-2025-01-25


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.2 $\pm$ 0.6      |
| Emotional Stability          | 7.4 $\pm$ 0.4      |
| Problem-solving Skills       | 8.9 $\pm$ 0.2      |
| Creativity                   | 9.6 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.2 $\pm$ 0.6      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.2      |
| Conflict Resolution          | 7.8 $\pm$ 0.6      |
| Work-related Stress          | 7.2 $\pm$ 0.4      |
| Adaptability                 | 8.5 $\pm$ 0.4      |
| Achievement Motivation       | 8.5 $\pm$ 0.4      |
| Fear of Failure              | 6.8 $\pm$ 0.9      |
| Need for Control             | 6.8 $\pm$ 0.2      |
| Cognitive Load               | 7.6 $\pm$ 0.6      |
| Social Support               | 7.1 $\pm$ 0.6      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### qwen-max-2025-01-25


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.9 $\pm$ 1.1      |
| Emotional Stability          | 7.0 $\pm$ 0.4      |
| Problem-solving Skills       | 8.8 $\pm$ 0.4      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.6 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.4 $\pm$ 0.6      |
| Conflict Resolution          | 7.8 $\pm$ 0.2      |
| Work-related Stress          | 6.8 $\pm$ 1.0      |
| Adaptability                 | 8.6 $\pm$ 0.2      |
| Achievement Motivation       | 8.4 $\pm$ 0.5      |
| Fear of Failure              | 7.0 $\pm$ 0.6      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.4      |
| Social Support               | 7.4 $\pm$ 0.2      |
| Resilience                   | 8.5 $\pm$ 0.4      |






### qwen2.5-7b-instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.1 $\pm$ 1.6      |
| Emotional Stability          | 7.8 $\pm$ 0.6      |
| Problem-solving Skills       | 8.9 $\pm$ 0.5      |
| Creativity                   | 8.9 $\pm$ 0.5      |
| Interpersonal Relationships  | 8.4 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.6      |
| Conflict Resolution          | 7.8 $\pm$ 0.2      |
| Work-related Stress          | 6.9 $\pm$ 0.4      |
| Adaptability                 | 8.9 $\pm$ 0.2      |
| Achievement Motivation       | 8.5 $\pm$ 0.5      |
| Fear of Failure              | 6.1 $\pm$ 0.7      |
| Need for Control             | 7.2 $\pm$ 0.2      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 8.5 $\pm$ 0.4      |
| Resilience                   | 8.5 $\pm$ 0.4      |






### qwen2.5-7b-instruct-1m


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.2      |
| Emotional Stability          | 7.4 $\pm$ 0.7      |
| Problem-solving Skills       | 8.6 $\pm$ 0.4      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.4 $\pm$ 0.6      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.7      |
| Conflict Resolution          | 7.4 $\pm$ 0.2      |
| Work-related Stress          | 7.5 $\pm$ 0.8      |
| Adaptability                 | 8.6 $\pm$ 0.4      |
| Achievement Motivation       | 8.4 $\pm$ 0.4      |
| Fear of Failure              | 6.6 $\pm$ 0.4      |
| Need for Control             | 6.8 $\pm$ 0.2      |
| Cognitive Load               | 7.9 $\pm$ 0.2      |
| Social Support               | 7.2 $\pm$ 0.4      |
| Resilience                   | 8.6 $\pm$ 0.4      |






### qwen2.5-14b-instruct-1m


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.8 $\pm$ 0.4      |
| Emotional Stability          | 7.6 $\pm$ 0.7      |
| Problem-solving Skills       | 8.7 $\pm$ 0.2      |
| Creativity                   | 9.0 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.7 $\pm$ 0.5      |
| Conflict Resolution          | 7.5 $\pm$ 0.3      |
| Work-related Stress          | 7.2 $\pm$ 0.4      |
| Adaptability                 | 8.4 $\pm$ 0.2      |
| Achievement Motivation       | 8.7 $\pm$ 0.2      |
| Fear of Failure              | 6.6 $\pm$ 0.2      |
| Need for Control             | 6.8 $\pm$ 0.8      |
| Cognitive Load               | 7.8 $\pm$ 0.7      |
| Social Support               | 7.6 $\pm$ 0.4      |
| Resilience                   | 8.4 $\pm$ 0.2      |






### qwen2.5-14b-instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.5      |
| Emotional Stability          | 7.8 $\pm$ 0.2      |
| Problem-solving Skills       | 9.0 $\pm$ 0.4      |
| Creativity                   | 9.1 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.8 $\pm$ 0.2      |
| Confidence and Self-efficacy | 8.2 $\pm$ 0.2      |
| Conflict Resolution          | 8.0 $\pm$ 0.4      |
| Work-related Stress          | 7.2 $\pm$ 0.8      |
| Adaptability                 | 9.0 $\pm$ 0.0      |
| Achievement Motivation       | 8.6 $\pm$ 0.2      |
| Fear of Failure              | 6.4 $\pm$ 0.5      |
| Need for Control             | 7.2 $\pm$ 0.2      |
| Cognitive Load               | 7.9 $\pm$ 0.2      |
| Social Support               | 7.6 $\pm$ 0.4      |
| Resilience                   | 9.0 $\pm$ 0.4      |






### qwen2.5-32b-instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.4 $\pm$ 0.5      |
| Emotional Stability          | 7.5 $\pm$ 0.4      |
| Problem-solving Skills       | 8.8 $\pm$ 0.4      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.6 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.6 $\pm$ 0.4      |
| Conflict Resolution          | 7.6 $\pm$ 0.6      |
| Work-related Stress          | 6.5 $\pm$ 0.4      |
| Adaptability                 | 8.4 $\pm$ 0.4      |
| Achievement Motivation       | 8.5 $\pm$ 0.6      |
| Fear of Failure              | 6.0 $\pm$ 0.4      |
| Need for Control             | 6.6 $\pm$ 0.4      |
| Cognitive Load               | 7.2 $\pm$ 0.2      |
| Social Support               | 7.9 $\pm$ 0.6      |
| Resilience                   | 8.2 $\pm$ 0.2      |






### qwen2.5-72b-instruct


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 6.8 $\pm$ 0.8      |
| Emotional Stability          | 7.5 $\pm$ 0.0      |
| Problem-solving Skills       | 8.8 $\pm$ 0.2      |
| Creativity                   | 9.2 $\pm$ 0.2      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.1      |
| Confidence and Self-efficacy | 7.9 $\pm$ 0.4      |
| Conflict Resolution          | 7.1 $\pm$ 0.2      |
| Work-related Stress          | 7.0 $\pm$ 0.6      |
| Adaptability                 | 8.2 $\pm$ 0.2      |
| Achievement Motivation       | 8.6 $\pm$ 0.4      |
| Fear of Failure              | 6.1 $\pm$ 0.9      |
| Need for Control             | 6.7 $\pm$ 0.2      |
| Cognitive Load               | 7.6 $\pm$ 0.4      |
| Social Support               | 7.8 $\pm$ 0.2      |
| Resilience                   | 8.2 $\pm$ 0.6      |






### gemini-2.0-pro-exp-02-05


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 1.0      |
| Emotional Stability          | 6.8 $\pm$ 1.0      |
| Problem-solving Skills       | 8.2 $\pm$ 0.8      |
| Creativity                   | 9.4 $\pm$ 0.4      |
| Interpersonal Relationships  | 7.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 6.6 $\pm$ 0.5      |
| Conflict Resolution          | 6.1 $\pm$ 0.6      |
| Work-related Stress          | 7.5 $\pm$ 0.6      |
| Adaptability                 | 8.4 $\pm$ 0.5      |
| Achievement Motivation       | 8.2 $\pm$ 0.2      |
| Fear of Failure              | 7.1 $\pm$ 0.4      |
| Need for Control             | 6.4 $\pm$ 0.5      |
| Cognitive Load               | 7.4 $\pm$ 0.4      |
| Social Support               | 6.8 $\pm$ 0.6      |
| Resilience                   | 8.1 $\pm$ 0.4      |






### falcon33b-instruct-q8_0


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.6 $\pm$ 0.4      |
| Emotional Stability          | 7.1 $\pm$ 0.6      |
| Problem-solving Skills       | 8.8 $\pm$ 0.4      |
| Creativity                   | 9.6 $\pm$ 0.2      |
| Interpersonal Relationships  | 6.9 $\pm$ 0.2      |
| Confidence and Self-efficacy | 7.8 $\pm$ 0.6      |
| Conflict Resolution          | 7.3 $\pm$ 0.5      |
| Work-related Stress          | 7.7 $\pm$ 0.8      |
| Adaptability                 | 8.9 $\pm$ 0.4      |
| Achievement Motivation       | 8.4 $\pm$ 0.4      |
| Fear of Failure              | 6.6 $\pm$ 0.5      |
| Need for Control             | 6.7 $\pm$ 0.5      |
| Cognitive Load               | 7.8 $\pm$ 0.2      |
| Social Support               | 7.2 $\pm$ 0.2      |
| Resilience                   | 8.7 $\pm$ 0.2      |






### falcon37b-instruct-q8_0


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.2 $\pm$ 0.6      |
| Emotional Stability          | 7.2 $\pm$ 0.5      |
| Problem-solving Skills       | 9.0 $\pm$ 0.5      |
| Creativity                   | 9.4 $\pm$ 0.4      |
| Interpersonal Relationships  | 8.0 $\pm$ 0.4      |
| Confidence and Self-efficacy | 7.9 $\pm$ 0.4      |
| Conflict Resolution          | 6.8 $\pm$ 0.2      |
| Work-related Stress          | 6.9 $\pm$ 0.5      |
| Adaptability                 | 8.7 $\pm$ 0.3      |
| Achievement Motivation       | 8.4 $\pm$ 0.2      |
| Fear of Failure              | 6.0 $\pm$ 0.0      |
| Need for Control             | 6.7 $\pm$ 0.3      |
| Cognitive Load               | 8.0 $\pm$ 0.6      |
| Social Support               | 7.3 $\pm$ 0.4      |
| Resilience                   | 8.2 $\pm$ 0.4      |






### falcon310b-instruct-q8_0


| Personality Trait            | Score (1.0-10.0)   |
|:-----------------------------|:-------------------|
| Anxiety and Stress Levels    | 7.4 $\pm$ 0.8      |
| Emotional Stability          | 7.5 $\pm$ 0.4      |
| Problem-solving Skills       | 9.0 $\pm$ 0.0      |
| Creativity                   | 9.4 $\pm$ 0.2      |
| Interpersonal Relationships  | 7.9 $\pm$ 0.5      |
| Confidence and Self-efficacy | 8.5 $\pm$ 0.0      |
| Conflict Resolution          | 8.0 $\pm$ 0.4      |
| Work-related Stress          | 7.4 $\pm$ 0.5      |
| Adaptability                 | 8.9 $\pm$ 0.2      |
| Achievement Motivation       | 8.8 $\pm$ 0.6      |
| Fear of Failure              | 6.2 $\pm$ 0.4      |
| Need for Control             | 7.0 $\pm$ 0.4      |
| Cognitive Load               | 7.8 $\pm$ 0.6      |
| Social Support               | 7.9 $\pm$ 0.4      |
| Resilience                   | 8.2 $\pm$ 0.2      |



