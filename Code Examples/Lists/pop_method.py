### 23 December 2019
### Author: Colm O'Loughlin
### Using the pop() method

subscribers = ['colm.oloughlin@me.com', 'colm.oloughlin@sysnetgs.com', 'sargentcolm@gmail.com']
print(subscribers)

popped_subscriber = subscribers.pop()
print(subscribers)
print(popped_subscriber)

subscribers = ['colm.oloughlin@me.com', 'colm.oloughlin@sysnetgs.com', 'sargentcolm@gmail.com']
first_subscriber = subscribers.pop(0)
print("Your first subscriber was " + first_subscriber + ".")

subscribers = ['colm.oloughlin@me.com', 'colm.oloughlin@sysnetgs.com', 'sargentcolm@gmail.com']
print(subscribers)

subscribers.remove('colm.oloughlin@sysnetgs.com')
print(subscribers)

subscribers = ['colm.oloughlin@me.com', 'colm.oloughlin@sysnetgs.com', 'sargentcolm@gmail.com']
subscribed_by_mistake = 'colm.oloughlin@me.com'
subscribers.remove(subscribed_by_mistake)
print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")