# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adiogo-f <adiogo-f@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/22 23:24:07 by adiogo-f          #+#    #+#              #
#    Updated: 2026/04/22 23:24:08 by adiogo-f         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))
    for i in range(1, n + 1):
        print("Day " + str(i))
    print("Harvest time!")
