% -------- Arithmetic Operations --------

add :-
    write('Enter first number: '), read(X),
    write('Enter second number: '), read(Y),
    R is X + Y,
    write('Result = '), write(R), nl.

subtract :-
    write('Enter first number: '), read(X),
    write('Enter second number: '), read(Y),
    R is X - Y,
    write('Result = '), write(R), nl.

multiply :-
    write('Enter first number: '), read(X),
    write('Enter second number: '), read(Y),
    R is X * Y,
    write('Result = '), write(R), nl.


% -------- Set Operations --------

read_list(List) :-
    write('Enter list (end with .): '),
    read(List),
    ( List == [] ->
        write('List is empty!'), nl
    ;
        true
    ).

union_set :-
    read_list(L1),
    read_list(L2),
    append(L1, L2, Temp),
    sort(Temp, R),
    write('Union = '), write(R), nl.

intersection_set :-
    read_list(L1),
    read_list(L2),
    findall(X, (member(X, L1), member(X, L2)), R),
    write('Intersection = '), write(R), nl.

difference_set :-
    read_list(L1),
    read_list(L2),
    findall(X, (member(X, L1), \+ member(X, L2)), R),
    write('Difference = '), write(R), nl.


% -------- Add Element --------

add_element :-
    read_list(L),
    write('Enter element to add: '), read(E),
    append(L, [E], NewList),
    write('New List = '), write(NewList), nl.


% -------- Menu --------

menu :-
    repeat,
    nl,
    write('---- MENU ----'), nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Union of Sets'), nl,
    write('5. Intersection of Sets'), nl,
    write('6. Difference of Sets'), nl,
    write('7. Add Element to List'), nl,
    write('8. Exit'), nl,
    write('Enter your choice: '),
    read(Choice),

    handle(Choice),
    Choice == 8, !.


% -------- Handle Choices --------

handle(1) :- add.
handle(2) :- subtract.
handle(3) :- multiply.
handle(4) :- union_set.
handle(5) :- intersection_set.
handle(6) :- difference_set.
handle(7) :- add_element.
handle(8) :- write('Exiting...'), nl.
handle(_) :- write('Invalid choice!'), nl.
