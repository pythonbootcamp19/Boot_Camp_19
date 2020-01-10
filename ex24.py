{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Let's practice everything.\n",
      "You'd need to know 'bout escapes with \\ that do:\n",
      "\n",
      " newlines and \t tabs.\n",
      "--------------------\n",
      "\n",
      "\n",
      "\tThe lovely world\n",
      "with logic so firmly planted\n",
      "cannot discern \n",
      " the needs of love\n",
      "nor comprehend passion from intution\n",
      "and requires an explanation\n",
      "\n",
      "\t\twhere there is none.\n",
      "\n",
      "--------------------\n",
      "This should be five: 5\n",
      "With a starting point of: 10000\n",
      "We'd have 5000000 beans, 5000.0 jars, and 50.0 crates.\n",
      "We can also do that this way:\n",
      "We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.\n"
     ]
    }
   ],
   "source": [
    "print(\"Let's practice everything.\")\n",
    "\n",
    "#\"\\\" is called string escaping\n",
    "\n",
    "print('You\\'d need to know \\'bout escapes with \\\\ that do:')\n",
    "\n",
    "print('\\n newlines and \\t tabs.')\n",
    "\n",
    "#\"\"\" \"\"\"multi line script. Good for paragraph. \n",
    "poem = \"\"\"\n",
    "\n",
    "\\tThe lovely world\n",
    "with logic so firmly planted\n",
    "cannot discern \\n the needs of love\n",
    "nor comprehend passion from intution\n",
    "and requires an explanation\n",
    "\\n\\t\\twhere there is none.\n",
    "\"\"\"\n",
    "\n",
    "print(\"--------------------\")\n",
    "print(poem)\n",
    "print(\"--------------------\")\n",
    "\n",
    "five = 10 - 2 + 3 - 6\n",
    "\n",
    "#f is string formatting\n",
    "print(f\"This should be five: {five}\")\n",
    "\n",
    "def secret_formula(started):\n",
    "    jelly_beans = started * 500\n",
    "    jars = jelly_beans / 1000\n",
    "    crates = jars / 100\n",
    "    return jelly_beans, jars, crates\n",
    "\n",
    "start_point = 10000\n",
    "beans, jars, crates = secret_formula(start_point)\n",
    "\n",
    "#remember that this is another way to format a string\n",
    "print(\"With a starting point of: {}\".format(start_point))\n",
    "\n",
    "#it's just like with an f\"\" string\n",
    "print(f\"We'd have {beans} beans, {jars} jars, and {crates} crates.\")\n",
    "start_point = start_point / 10\n",
    "\n",
    "print(\"We can also do that this way:\")\n",
    "formula = secret_formula(start_point)\n",
    "#this is an easy way to apply a list to a format strting\n",
    "#\".format(*variable name you want to unpack)\" in the below is unpacking the variables\n",
    "print(\"We'd have {} beans, {} jars, and {} crates.\".format(*formula))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "EOL while scanning string literal (<ipython-input-5-5fa11007ade9>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-5-5fa11007ade9>\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    print(f\"My name is {name}, I live in {city} and I am from {hometown})\u001b[0m\n\u001b[0m                                                                         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m EOL while scanning string literal\n"
     ]
    }
   ],
   "source": [
    "name = \"Vik\"\n",
    "city = \"Bangalore\"\n",
    "hometown = \"Mumbai\"\n",
    "print(f\"My name is {name}, I live in {city} and I am from {hometown})\n",
    "print(\"My name is {}, I live in {} and I am from {}\". format(name, city, town))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def take_input():\n",
    "      name = input(\"Enter your name\")\n",
    "      age = input(\"Enter your age\")\n",
    "      city = input(\"Enter your city\")\n",
    "      return name, age, city\n",
    "      \n",
    "      user_data = take_input()\n",
    "      print(user_data)\n",
    "      \n",
    "      #In the following example we are unpacking the data in a couple of ways(.format(*user_data))\n",
    "      name, age, city = user_data\n",
    "      print(\"user name is {} user age is {} and user city is {}\".format(*user_data))\n",
    "      print(\"user name is {} user age is {} and user city is {}\".format(name, age, city))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
