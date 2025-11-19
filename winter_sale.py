d,p=map(int,input().split())
original_price=p/(1-(d/100))
print(f"{original_price:.2f}")

# original price -(original price*discount/100)=price after discount
# so taking original price common from eqn
# ORIgINAL PRICE=price ater discount/(1-D/100)