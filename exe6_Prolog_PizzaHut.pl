:- dynamic price/2, order/3.

% -------- MENU ITEMS --------
item(1, margherita).
item(2, pepperoni).
item(3, veggie).
item(4, chicken).
item(5, pasta).
item(6, bread).

% -------- STEP 1: GET PRICES --------
set_prices :-
    item(_, Item),
    write('Enter price for '), write(Item), write(': '),
    read(P),
    assert(price(Item, P)),
    fail.
set_prices.

% -------- STEP 2: DISPLAY MENU WITH PRICES --------
show_menu :-
    nl, write('------ MENU WITH PRICES ------'), nl,
    item(N, Item),
    price(Item, Price),
    write(N), write('. '), write(Item),
    write(' - Rs.'), write(Price), nl,
    fail.
show_menu.

% -------- STEP 3: TAKE ORDER --------
take_order :-
    write('Enter item number (0 to stop): '),
    read(Choice),
    handle_order(Choice).

handle_order(0) :- !.

handle_order(Choice) :-
    item(Choice, Item),
    price(Item, Price),
    write('Enter quantity: '),
    read(Qty),
    assert(order(Item, Qty, Price)),
    take_order.

% -------- STEP 4: PRINT ORDER DETAILS --------
print_orders :-
    nl, write('------ ORDER DETAILS ------'), nl,
    order(Item, Qty, Price),
    Sub is Qty * Price,

    write('Item: '), write(Item), nl,
    write('Price: '), write(Price), nl,
    write('Quantity: '), write(Qty), nl,
    write('Subtotal: '), write(Sub), nl,
    write('-------------------------'), nl,

    fail.
print_orders.

% -------- STEP 5: TOTAL --------
calculate_total(Total) :-
    findall(Sub, (order(_, Q, P), Sub is Q*P), List),
    sum_list(List, Total).

% -------- FINAL BILL --------
final_bill :-
    print_orders,
    calculate_total(Total),
    nl,
    write('TOTAL AMOUNT = '), write(Total), nl.

% -------- MAIN --------
start :-
    set_prices,
    show_menu,
    take_order,
    final_bill.
