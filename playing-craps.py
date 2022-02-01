{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3325ad2a-9d55-481d-9576-e6b9eadfa297",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Face    Frequency\n",
      "   1            0\n",
      "   2       166370\n",
      "   3       333826\n",
      "   4       501505\n",
      "   5       665611\n",
      "   6       834351\n",
      "   7      1001471\n",
      "   8       830617\n",
      "   9       667352\n",
      "  10       499831\n",
      "  11       332628\n",
      "  12       166438\n",
      "craps 0.11110566666666667\n",
      "win 0.22234983333333333\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "frequency1 = 0\n",
    "frequency2 = 0\n",
    "frequency3 = 0\n",
    "frequency4 = 0\n",
    "frequency5 = 0\n",
    "frequency6 = 0\n",
    "frequency7 = 0\n",
    "frequency8 = 0\n",
    "frequency9 = 0\n",
    "frequency10 = 0\n",
    "frequency11 = 0\n",
    "frequency12 = 0\n",
    "\n",
    "trials = 6_000_000\n",
    "for roll in range(trials):\n",
    "    face = random.randrange(1, 7) + random.randrange(1, 7)\n",
    "\n",
    "    if face == 1: \n",
    "      frequency1 += 1\n",
    "    elif face == 2: \n",
    "      frequency2 += 1\n",
    "    elif face == 3: \n",
    "      frequency3 += 1\n",
    "    elif face == 4: \n",
    "      frequency4 += 1\n",
    "    elif face == 5: \n",
    "      frequency5 += 1\n",
    "    elif face == 6: \n",
    "      frequency6 += 1\n",
    "    elif face == 7: \n",
    "      frequency7 += 1\n",
    "    elif face == 8: \n",
    "      frequency8 += 1\n",
    "    elif face == 9: \n",
    "      frequency9 += 1\n",
    "    elif face == 10: \n",
    "      frequency10 += 1\n",
    "    elif face == 11: \n",
    "      frequency11 += 1\n",
    "    elif face == 12: \n",
    "      frequency12 += 1\n",
    "    \n",
    "print(f'Face{\"Frequency\":>13}')\n",
    "print(f'{1:>4}{frequency1:>13}')\n",
    "print(f'{2:>4}{frequency2:>13}')\n",
    "print(f'{3:>4}{frequency3:>13}')\n",
    "print(f'{4:>4}{frequency4:>13}')\n",
    "print(f'{5:>4}{frequency5:>13}')\n",
    "print(f'{6:>4}{frequency6:>13}')\n",
    "print(f'{7:>4}{frequency7:>13}')\n",
    "print(f'{8:>4}{frequency8:>13}')\n",
    "print(f'{9:>4}{frequency9:>13}')\n",
    "print(f'{10:>4}{frequency10:>13}')\n",
    "print(f'{11:>4}{frequency11:>13}')\n",
    "print(f'{12:>4}{frequency12:>13}')\n",
    "\n",
    "craps = frequency2 + frequency3 + frequency12\n",
    "win = frequency7 + frequency11\n",
    "print ('craps', craps/trials)\n",
    "print ('win', win/trials)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ce773d9-db71-490a-a89a-874d1b907f67",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

