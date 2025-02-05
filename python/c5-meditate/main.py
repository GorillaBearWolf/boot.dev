def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana and energy + energy_drinks > 0:

        if energy_drinks and not energy:
            energy_drinks -= 1
            energy += 50

        energy -= 1
        mana += 1


    return mana, energy, energy_drinks
