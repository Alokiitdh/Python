print('welcome to bidding')

bidder_data = {}

# making bidder data
def bidder(name, bid):
    bidder_data[name] = bid
    return bidder_data



more_bidder = 'y'
while(more_bidder=='y'):
    name = input('Bidder Name: ')
    bid = int(input('Enter bid: '))
    print(bidder(name, bid))
    print('\n'*100)
    more_bidder = input('Are there any bidder(y/n): ')

## checking who won the bid
max_bid = 0
for key in bidder_data:
    if bidder_data[key] > max_bid:
        max_bid = bidder_data[key]
        winner = key

print(f'{winner} won with {bidder_data[winner]} bid')
print()
    
    

## printing biider name and its bid






