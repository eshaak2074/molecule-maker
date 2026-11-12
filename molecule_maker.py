from drafter import *
from bakery import assert_equal
from lewis_structures import *
from three_d_structures import *
from dataclasses import dataclass

set_website_title("Molecule Maker")
set_site_information(
    author="Ella Shaak",
    description="Learning model to create chemical molecules",
    sources="",
    planning=[],
    links=[]
)
hide_debug_information()

@dataclass
class Nonmetal:
    symbol: str
    valence_electrons: int
    
@dataclass
class Molecule:
    molecule_symbol_name: str
    valence_electrons: int
    
@dataclass
class State:
    nonmetal_one: Nonmetal
    nonmetal_two: Nonmetal
    bonded: Molecule
    history: list[Molecule]

def determine_element(element: str) -> str:
    """
    This function determines the element name based on the symbol provided.
    
    Args:
        element: the symbol of an element as a str
    
    Returns:
        A str of the name of the element
    """  
    if element == "N":
        return "Nitrogen"
    elif element == "H":
        return "Hydrogen"
    elif element == "O":
        return "Oxygen"
    elif element == "F":
        return "Fluorine"
    elif element == "C":
        return "Carbon"
    else:
        return "invalid"
    
assert_equal(determine_element("N"), "Nitrogen")
assert_equal(determine_element("C"), "Carbon")
assert_equal(determine_element("E"), "invalid")
    
def determine_valence_electrons(element: str) -> int:
    """
    This function determines the amount of valence electrons the element has given an element.
    
    Args:
        element: the name of the element as a str
        
    Returns:
        An int of the number of valence electrons the element has
    """
    if element == "Nitrogen":
        return 5
    if element == "Hydrogen":
        return 1
    if element == "Oxygen":
        return 6
    if element == "Fluorine":
        return 7
    if element == "Carbon":
        return 4
    
assert_equal(determine_valence_electrons("Nitrogen"), 5)
assert_equal(determine_valence_electrons("Oxygen"), 6)
assert_equal(determine_valence_electrons("Carbon"), 4)
    
def determine_molecule(element: str, element_two: str) -> str:
    """
    This function determines the most common molecule for every combination given two elements.
    
    Args:
        element: the symbol of the first element
        element_two: the symbol of the second element
    
    Returns:
        A str is return of the most common molecule depending on the combination of elements
    """
    if element == "N":
        if element_two == "N":
            return "N₂ (Dinitrogen)"
        if element_two == "H":
            return "NH₃ (Ammonia)"
        if element_two == "O":
            return "NO (Nitric Oxide)"
        if element_two == "C":
            return "NCN (Cyanonitrene Radical)"
        if element_two == "F":
            return "NF₃ (Nitrogen Trifluoride)"
    elif element == "H":
        if element_two == "N":
            return "NH₃ (Ammonia)"
        if element_two == "H":
            return "H₂ (Dihydrogen)"
        if element_two == "O":
            return "H₂O (Water)"
        if element_two == "C":
            return "CH₄ (Methane)"
        if element_two == "F":
            return "HF (Hydrogen Fluoride)"
    elif element == "O":
        if element_two == "N":
            return "NO (Nitric Oxide)"
        if element_two == "H":
            return "H₂O (Water)"
        if element_two == "O":
            return "O₂ (Dioxygen)"
        if element_two == "C":
            return "CO₂ (Carbon Dioxide)"
        if element_two == "F":
            return "OF₂ (Oxygen Difluoride)"
    elif element == "C":
        if element_two == "N":
            return "NCN (Cyanonitrene Radical)"
        if element_two == "H":
            return "CH₄ (Methane)"
        if element_two == "O":
            return "CO₂ (Carbon Dioxide)"
        if element_two == "C":
            return "C₂ (Dicarbon)"
        if element_two == "F":
            return "CF₄ (Carbon Tetrafluoride)"
    elif element == "F":
        if element_two == "N":
            return "NF₃ (Nitrogen Trifluoride)"
        if element_two == "H":
            return "HF (Hydrogen Fluoride)"
        if element_two == "O":
            return "OF₂ (Oxygen Difluoride)"
        if element_two == "C":
            return "CF₄ (Carbon Tetrafluoride)"
        if element_two == "F":
            return "F₂ (Difluorine)"

assert_equal(determine_molecule("H", "H"), "H₂ (Dihydrogen)")
assert_equal(determine_molecule("N", "F"), "NF₃ (Nitrogen Trifluoride)")
assert_equal(determine_molecule("F", "N"), "NF₃ (Nitrogen Trifluoride)")
        
def determine_molecule_index(molecule: str) -> int:
    """
    This function determines the index of molecule that will be used to determine which image to use.
    
    Args:
        molecule: A str of the molecule
        
    Returns:
        An int representing the index for the molecule
    """
    if molecule == "N₂ (Dinitrogen)":
        return 0
    elif molecule == "NH₃ (Ammonia)":
        return 1
    elif molecule == "NO (Nitric Oxide)":
        return 2
    elif molecule == "NCN (Cyanonitrene Radical)":
        return 3
    elif molecule == "NF₃ (Nitrogen Trifluoride)":
        return 4
    elif molecule == "H₂ (Dihydrogen)":
        return 5
    elif molecule == "H₂O (Water)":
        return 6
    elif molecule == "CH₄ (Methane)":
        return 7
    elif molecule == "HF (Hydrogen Fluoride)":
        return 8
    elif molecule == "O₂ (Dioxygen)":
        return 9
    elif molecule == "CO₂ (Carbon Dioxide)":
        return 10
    elif molecule == "OF₂ (Oxygen Difluoride)":
        return 11
    elif molecule == "C₂ (Dicarbon)":
        return 12
    elif molecule == "CF₄ (Carbon Tetrafluoride)":
        return 13
    elif molecule == "F₂ (Difluorine)":
        return 14

assert_equal(determine_molecule_index("CH₄ (Methane)"), 7)
assert_equal(determine_molecule_index("C₂ (Dicarbon)"), 12)
assert_equal(determine_molecule_index("H₂O (Water)"), 6)
    
def determine_total_valence_electrons(molecule: str) -> int:
    """
    This function determines the total valence electrons a given molecule has.
    
    Args:
        molecule: A str of the symbol and name of the molecule
        
    Returns:
        An int of the number of electrons the molecule has
    """
    if molecule == "N₂ (Dinitrogen)":
        return 10
    elif molecule == "NH₃ (Ammonia)":
        return 8
    elif molecule == "NO (Nitric Oxide)":
        return 11
    elif molecule == "NCN (Cyanonitrene Radical)":
        return 14
    elif molecule == "NF₃ (Nitrogen Trifluoride)":
        return 26
    elif molecule == "H₂ (Dihydrogen)":
        return 2
    elif molecule == "H₂O (Water)":
        return 8
    elif molecule == "CH₄ (Methane)":
        return 8
    elif molecule == "HF (Hydrogen Fluoride)":
        return 8
    elif molecule == "O₂ (Dioxygen)":
        return 12
    elif molecule == "CO₂ (Carbon Dioxide)":
        return 16
    elif molecule == "OF₂ (Oxygen Difluoride)":
        return 20
    elif molecule == "C₂ (Dicarbon)":
        return 8
    elif molecule == "CF₄ (Carbon Tetrafluoride)":
        return 32
    elif molecule == "F₂ (Difluorine)":
        return 14
    
assert_equal(determine_total_valence_electrons("H₂O (Water)"), 8)
assert_equal(determine_total_valence_electrons("CF₄ (Carbon Tetrafluoride)"), 32)
assert_equal(determine_total_valence_electrons("CO₂ (Carbon Dioxide)"), 16)
    
@route
def index(state: State) -> Page:
    """
    This route takes in the state and returns a Page that is the Home Page of the website.
    It allows for user input in a TextBox and check thats it's valid. It also provides the option
    to show the created molecule history once a molecule has been appended to history in the state
    dataclass.
    
    Args:
        state: the current state the website as State
        
    Returns:
        A Page describe the home page of the website
    """
    if state.history == []:
        return Page(state, [
                Header("Molecule Maker"),
                "N, H, O, F, C",
                "\n \n Enter an element from the provided list above of nonmetals",
                "\n Element:",
                TextBox("element"),
                Button("Find Match", "determine_valid_nonmetal"),
                "\n \n You have no history of molecules!"
            ])
    else:
        return Page(state, [
                Header("Molecule Maker"),
                "N, H, O, F, C",
                "\n \n Enter an element from the provided list above of nonmetals",
                "\n Element:",
                TextBox("element"),
                Button("Find Match", "determine_valid_nonmetal"),
                "\n\n Click to view History:",
                Button("View History", "show_history"),
                "Show Structures:",
                CheckBox("show_structures", False)
            ])
    
@route
def show_history (state: State, show_structures: bool) -> Page:
    """
    This route shows the history of the molecules you have created. This can only
    be acessed when a molecule has been apended to the history. The page shows the
    names of all the molecules you have created and if the check box is selected to
    show structures, the only the structures will be shown.
    
    Args:
        state: the current state of the website as State
        show_structures: CheckBox as a bool to show the structures of the molecules
        
    Returns:
        The Page that shows the history of molecules or structures depending on the
        CheckBox
    """
    if show_structures == False:
        total = 0
        molecules = ""
        for molecule in state.history:
            total = total + 1
            molecules = molecules + molecule.molecule_symbol_name + "\n" 
        if total == 1:
            return Page(state, [
                    Header("You have made " + str(total) + " molecule"),
                    molecules + "\n",
                    Button("Return Home", "index")
                ]) 
        else:
            return Page(state, [
                Header("You have made " + str(total) + " molecules"),
                molecules + "\n",
                Button("Return Home", "index")
                ])
    else:
        structures = []
        total = 0
        for molecule in state.history:
            index = determine_molecule_index(molecule.molecule_symbol_name)
            structure = Image(three_d[index], 500)
            structures.append(structure)
            total = total + 1
        return_page = []
        if total == 1:
            return_page.append(Header("You have made " + str(total) + " molecule"))
        else:
            return_page.append(Header("You have made " + str(total) + " molecules"))
        for structure in structures:
            return_page.append(structure)
        return_page.append(Button("Return Home", "index"))
        return Page(state, return_page)

@route
def determine_valid_nonmetal(state: State, element: str) -> Page:
    """
    This route takes in a state and the element entered by the suer and returns a Page
    depending if the element is valid or not. If the element is valid it returns a Page
    to bond the element you selected with a SelectBox and assigns element to the state.
    If the element is invalid, it promts you to try again and return to home using index.
    
    Args:
        state: the current state of the website as State
        element: the user inputed element as a str
        
    Returns:
        The Page showing either that an invalid element was entered or a SelectBox to bond
        your element.
    """
    state.nonmetal_one.symbol = element
    options = ["N", "H", "O", "C", "F"]
    element_name = determine_element(element)
    if element_name == "invalid":
        return Page(state, [
                Header("You selected an Invalid Element!"),
                "Please try again:",
                Button("Return Home", "index")
            ])
    else:
        valence_electrons = determine_valence_electrons(element_name)
        state.nonmetal_one.valence_electrons = valence_electrons
        return Page(state, [
                    Header("You Selected " + element_name),
                    "Select an element to bond your nonmetal",
                    "\n Element:",
                    SelectBox("element_two", options, options[0]),
                    Button("Bond", "bond")
            ])
   
@route
def bond(state: State, element_two: str) -> Page:
    """"
    This route takes in the state of the website and element_two from the SelectBox
    and returns a Page describing the molecule you have created. It shows the name
    of the molecule and the options with Buttons to show information about the molecule
    or show its lewis structure. Additionally, the molecule is assigned to the state
    and appended to the history in the state, and the valence electrons are assigned
    in the state. 
    
    Args:
        state: the state of the website as a State
        element_two: the element entered from the SelectBox as a str
        
    Returns:
        A Page describing the molecule that has been created
    """
    state.nonmetal_two.symbol = element_two
    element = state.nonmetal_one.symbol
    valence_electrons = determine_valence_electrons(determine_element(element_two))
    state.nonmetal_two.valence_electrons = valence_electrons
    molecule = determine_molecule(element, element_two)
    valence_electrons = determine_total_valence_electrons(molecule)
    state.bonded = Molecule(molecule, valence_electrons)
    state.history.append(Molecule(molecule, valence_electrons))
    return Page(state, [
            Header("You created a Molecule!"),
            "Bonding " + element + " and " + element_two + " creates " + state.bonded.molecule_symbol_name + "\n\n",
            Button("Show Information", "show_information"),
            Button("Show Lewis Structure", "show_lewis_structure")
        ])

@route
def show_information(state: State) -> Page:
    """
    This route takes in the state of the website and returns a Page listing information
    about the molecule you have created. It lists information about the amount of
    valence electrons each element has and the total electrons the molecule has.
    
    Args:
        state: the current state of the website as State
    
    Returns:
        A page describing information about the molecule created
    """
    return Page(state, [
            Header("Information About Your Molecule"),
            state.nonmetal_one.symbol + " has " + str(state.nonmetal_one.valence_electrons) + " valence electrons and " + state.nonmetal_two.symbol + " has " + str(state.nonmetal_two.valence_electrons) + " valence electrons",
            "\n" + state.bonded.molecule_symbol_name + " has a total of " + str(state.bonded.valence_electrons) + " valence electrons",
            Button("Show Lewis Structure", "show_lewis_structure")
        ])

@route
def show_lewis_structure(state: State) -> Page:
    """
    This route takes in the state of the webiste and returns a Page showing the
    lewis structure of the molecule created. The page shows the image of the
    lewis structuture of the molecule and promts the user to show the information
    of the molecule, show the 3D structure of the molecule, or return back to the
    home page.
    
    Args:
        state: the current state of the website as State
        
    Returns:
        A Page showing the image of the lewis structure of the molecule created
    """
    molecule = state.bonded.molecule_symbol_name
    index = determine_molecule_index(molecule)
    return Page(state, [
            Header("This is the Lewis Structure of " + state.bonded.molecule_symbol_name),
            Image(lewis[index], 500),
            "\n\n",
            Button("Show Information", "show_information"),
            Button("Show 3D Structure", "show_three_d"),
            Button("Return Home", "index")
        ])

@route
def show_three_d(state: State) -> Page:
    """
    This route takes in the current state and returns a Page showing the 3D structure
    of the molecule created. It shows the image of the 3D structure of the molecule and
    promts the user to return home or return back to the lewis structure page.
    
    Args:
        state: the current state of the website as State
        
    Returns:
        A Page showing the image of the 3D structure of the molecule created
    """
    molecule = state.bonded.molecule_symbol_name
    index = determine_molecule_index(molecule)
    return Page(state, [
            Header("This is the 3D Structure of " + state.bonded.molecule_symbol_name),
            Image(three_d[index], 500),
            "\n\n",
            Button("Return Home", "index"),
            Button("Return Back to Lewis Structure", "show_lewis_structure")
        ])

"""
possible improvements:
    clear history button
    show information where hydrogen says 1 valence electron
"""

start_server(State(Nonmetal("", 0), Nonmetal("", 0), Molecule("", 0), []))
