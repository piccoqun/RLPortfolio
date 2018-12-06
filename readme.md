# Reference
This is a Reinforcement Learning portfolio management strategy based on
the paper of A Deep Reinforcement Learning Framework for the Financial
Portfolio Management Problem".

The method jumped the process of price prediction in the portfolio
construction workflow and made market actions directly from the
states based on the financial market environment.

Source Code: https://github.com/ZhengyaoJiang/PGPortfolio

## Changes from the Original Paper
### Data
The paper used cryptocurrency for data testing. We changed it to daily
stock price, as long as the hypothesis of Zero Slippage and Zero Market
 Impact stand.

### RL Reward
The paper set the cumulated portfolio return as the RL reward. To combine
risk in the portfolio decision, we can add max drawdown as risk into the objective
function.