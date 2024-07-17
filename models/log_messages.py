# SINGLETON EXCEPTION
def instance_exists_error(class_name):
    return f"An instance of {class_name} already exists. Use get_instance() to access it."


# Path Messages
NO_TOP_LEVEL_FILE = "There is No Top Level File"
QUARTUS_PATH_SPECIFIED = "Quartus Path Specified Successfully."
NO_QUARTUS_PATH = "No Quartus Path Specified."
NO_SOF_FILE = "There is no Sof File. Try Synthesis"
ENV_PATH_SET = "Quartus Environment Path Set Successfully."
NO_ENV_PATH = "NO Quartus Environment Path Specified"

# UART Messages
UART_RESET = "UART Configurations is Reset."
UART_CONFIG_SET = "UART Configurations Set Successfully."

# SPI Messages
SPI_RESET = "SPI Configurations is Reset."
SPI_CONFIG_SET = "SPI Configurations Set Successfully."

# Synthesize Messages
SYNTHESIZE_INITIATED = "Synthesizing Process Initiated. Please Await Completion..."
SYNTHESIZE_SUCCESS = "Synthesizing Process Completed Successfully in:"
SYNTHESIZE_FAILED = "Synthesizing Process Failed. Please review and try again."

# Sniffing Messages
SNIFFING_TIME_WARNING = "Sniffing Data Time Exceeds 2 Hours, Data Will Be Sniffed Until 2 Hours Only."
NO_CONFIGURATIONS_FOUND = "There is No Configurations Found."
SNIFFING_STARTED = 'Sniffing Started Successfully ...'

# Receiving Data Messages
RECEIVED_SUCCESS = "Data Received Successfully."
TIME_SNIFFING_FINISHED = "Sniffing Finished Successfully."
SNIFFING_NOT_FINISHED = "Sniffing Still Running..."
FTP_NOT_OPENED = "FTP Not Opened."

# Serial Communication
SENDING_SUCCESS = "Data Send Successfully"
RECEIVE_SUCCESS = "Data Received Successfully"
PORT_NOT_OPEN_ERROR = "Port is not open"
TIMEOUT_ERROR = "Timeout in Sending Data"
CONFIGURATION_ERROR = "Device Can Not Be Found or Can Not Be Configured"
CONFIGURATION_SUCCESS = "The Tool is Configured Successfully"

# Bit Sniffing Messages
ONE_BIT_CONFIG_SET = "One Bit Sniffing Configurations Set Successfully."
N_BITS_CONFIG_SET = "N Bits Sniffing Configurations Set Successfully."
NUMBER_BITS_RESET = "Number Bits Configuration is Reset."

# Hardware Pin Planner
PINS_SET = "Hardware Pins Set Successfully."
PINS_NUMBERS = [
    'PIN_1', 'PIN_2', 'PIN_3 - ', 'PIN_7', 'PIN_10', 'PIN_11', 'PIN_23', 'PIN_25', 'PIN_28', 'PIN_30',
    'PIN_31', 'PIN_32', 'PIN_33', 'PIN_34', 'PIN_38', 'PIN_39', 'PIN_42', 'PIN_43', 'PIN_44', 'PIN_46',
    'PIN_49', 'PIN_50', 'PIN_51', 'PIN_52', 'PIN_53', 'PIN_54', 'PIN_55', 'PIN_58', 'PIN_59', 'PIN_60',
    'PIN_64', 'PIN_65', 'PIN_66', 'PIN_67', 'PIN_68', 'PIN_69', 'PIN_70', 'PIN_71', 'PIN_72', 'PIN_73',
    'PIN_74', 'PIN_75', 'PIN_76', 'PIN_77', 'PIN_80', 'PIN_83', 'PIN_84', 'PIN_85', 'PIN_86', 'PIN_87',
    'PIN_88', 'PIN_89', 'PIN_90', 'PIN_91', 'PIN_98', 'PIN_99', 'PIN_100', 'PIN_101', 'PIN_103', 'PIN_104',
    'PIN_105', 'PIN_106', 'PIN_110', 'PIN_112', 'PIN_113', 'PIN_114', 'PIN_115', 'PIN_119', 'PIN_120',
    'PIN_121', 'PIN_124', 'PIN_125', 'PIN_126', 'PIN_127', 'PIN_128', 'PIN_129', 'PIN_132', 'PIN_133',
    'PIN_135', 'PIN_136', 'PIN_137', 'PIN_138', 'PIN_141', 'PIN_142', 'PIN_143', 'PIN_144'
]
PINS_RESET = "Hardware Pins Configuration is Reset."

# Display Button Messages
DATA_DISPLAYED = "Selected Data Displayed Successfully"
NO_TIMESTAMP_SET = "No Selected Data to Display"
NO_LAST_ID_DATA = "No Data Stored to Display"


# Intercept Messages
REPLAY_ATTACK_SUCCESS = "Replay Attack Started Successfully"
STREAM_FINDER_SUCCESS = "Stream Finder Started Successfully"
CONDITIONAL_BYPASS_SUCCESS = "Conditional Bypass Started Successfully"
NO_STREAM_FINDER_INPUT = "No Input Data Stream Entered"
NO_STREAM_FINDER_ACTION = "No Stream Finder Action Selected"
NO_INTERCEPT_TERMINAL_DATA = "No Data Found in The Intercept Terminal"
NO_CUSTOM_TERMINAL_DATA = "No Data Found in The Custom Data Terminal"
CONDITION_FOUND = "Stream Found and Communication Stopped"
CONDITION_NOT_FOUND = "Stream Not Found and Communication Passed"

# Fuzzing Messages
DATA_TYPE_ERROR = "No selected data type"
NO_NUMBER_OF_MESSAGES = "Number of messages not found"
NEGATIVE_NUMBER_OF_MESSAGES = "Value error. Number of messages can't be negative"
NO_NUMBER_OF_BYTES = "Number of bytes not found"
NEGATIVE_NUMBER_OF_BYTES = "Value error. Number of bytes can't be negative"
NO_FUZZING_ON = "Fuzzing on not found"
NO_SNIFFING_ON = "Sniffing on not found"
NO_FUZZING_MODE = "Fuzzing mode not found"

NO_GENERATED_DATA = "There is no generation data to send"
NO_SELECTED_ROWS = "No selected rows from table to send"
START_END_RANGE_NOT_EXIST = "Start or End range is not provided"
START_END_RANGE_ERROR = "Start or End row is out of range"

FUZZING_DATA_GENERATED = "Fuzzing messages Generated Successfully"
FUZZING_MESSAGES_SEND = "Fuzzing messages sent successfully"
FUZZING_MESSAGES_RESPONSE_RECEIVE = "Fuzzing messages and responses received successfully"

LOAD_DATA_NO_FILE = "File CSV not found"
LOAD_DATA_ERROR = "Error loading CSV file"
