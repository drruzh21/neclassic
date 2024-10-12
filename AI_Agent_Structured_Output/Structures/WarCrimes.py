from dotenv import load_dotenv

from AI_Agent_Structured_Output.AbstractStructure import AbstractStructure

load_dotenv()

from pydantic import Field
from typing import Optional


class ProductCriteria14(AbstractStructure):
    completeness: Optional[str] = Field(None,
                                        description="Indicates the level of completeness of the product, crucial for understanding functionality.")
    category: Optional[str] = Field(None, description="Helps classify products based on intended use or duty level.")
    color: Optional[str] = Field(None,
                                 description="A significant differentiator in product selection, especially for visibility.")
    size: Optional[str] = Field(None,
                                description="Critical for ensuring the right fit and comfort. Ensure size measurements are in meters (SI units). If input is in other units, convert to meters.")
    signs_of_difference: Optional[str] = Field(None,
                                               description="Indicates unique features or certifications influencing purchasing decisions.")
    volume: Optional[str] = Field(None,
                                  description="Relevant for products where size or capacity is a consideration. Ensure volume measurements are in cubic meters (SI units). If input is in other units, convert to cubic meters.")
    material: Optional[str] = Field(None,
                                    description="Important for understanding durability and suitability for specific environments.")
    protection_class: Optional[str] = Field(None,
                                            description="Crucial for safety products, indicating the level of protection offered.")
    temperature_protection: Optional[str] = Field(None,
                                                  description="Relevant for products needing to withstand specific temperature conditions. Ensure temperature is measured in Kelvin or Celsius (SI units). If input is in other units, convert to SI.")
    climate_zones: Optional[str] = Field(None,
                                         description="Important for understanding suitability for different environmental conditions.")
    size_range: Optional[str] = Field(None,
                                      description="Provides additional information about flexibility in sizing options. Ensure size range measurements are in meters (SI units). If input is in other units, convert to meters.")
    regulations: Optional[str] = Field(None, description="Important for compliance with industry standards.")


class ProductCriteria27(AbstractStructure):
    voltage_rating: Optional[str] = Field(None,
                                          description="Indicates the maximum voltage the product can safely handle, ensuring compatibility with electrical systems.")
    current_rating: Optional[str] = Field(None,
                                          description="Specifies the maximum current the product can carry without overheating, which is crucial for safety and performance.")
    number_of_conductors: Optional[str] = Field(None,
                                                description="Indicates the number of separate wires within the cable, affecting functionality and application in electrical systems.")
    insulation_material: Optional[str] = Field(None,
                                               description="Specifies the type of insulation material, which affects durability, flexibility, and safety under different environmental conditions.")
    cross_section_area: Optional[str] = Field(None,
                                              description="Represents the cross-sectional area of the conductor, important for determining current-carrying capacity and electrical resistance.")
    fire_hazard: Optional[str] = Field(None,
                                       description="Indicates the product's safety level in terms of fire risk, crucial for compliance with safety standards.")
    frost_resistance: Optional[str] = Field(None,
                                            description="Indicates the product's ability to maintain functionality and safety in cold environments.")
    weight: Optional[str] = Field(None,
                                  description="Specifies the weight of the product, relevant for installation and handling, particularly in larger applications.")
    diameter: Optional[str] = Field(None,
                                    description="Specifies the outer diameter of the product, relevant for compatibility with connectors and conduits.")
    color: Optional[str] = Field(None,
                                 description="Indicates the color of the product, which can be important for identification and safety purposes.")
    temperature_range: Optional[str] = Field(None,
                                             description="Indicates the operational temperature limits, ensuring the product can function in its intended environment.")
    screen_type: Optional[str] = Field(None,
                                       description="Specifies the type of screen used to provide electromagnetic interference (EMI) protection, important in sensitive electrical applications.")
    sheath_material: Optional[str] = Field(None,
                                           description="Specifies the material used for the outer sheath, contributing to the product's durability and environmental resistance.")


class ProductCriteria28(AbstractStructure):
    weight: Optional[str] = Field(None,
                                  description="Specifies the weight of the product, crucial for understanding portability, handling, and installation requirements.")
    dimensions: Optional[str] = Field(None,
                                      description="Indicates the physical dimensions of the product, ensuring compatibility with existing systems or spaces.")
    power: Optional[str] = Field(None,
                                 description="Represents the power rating of the product, crucial for evaluating performance and efficiency, especially for machinery and tools.")
    completeness: Optional[str] = Field(None,
                                        description="Indicates the completeness of the product, including the number of included components, important for assessing value and usability.")
    category: Optional[str] = Field(None,
                                    description="Helps classify products based on intended use, providing context for evaluating features and performance.")
    torque: Optional[str] = Field(None,
                                  description="Specifies the torque value, important for assessing the effectiveness of mechanical applications.")
    speed: Optional[str] = Field(None,
                                 description="Indicates the operational speed, relevant for evaluating the efficiency and performance of rotating machinery.")
    filtration_degree: Optional[str] = Field(None,
                                             description="Represents the filtration degree, crucial for assessing the effectiveness of products related to fluid dynamics or filtration.")
    chuck_diameter: Optional[str] = Field(None,
                                          description="Specifies the chuck diameter, relevant for tools that require specific attachments or fittings, impacting versatility.")
    rotation_speed: Optional[str] = Field(None,
                                          description="Indicates the rotation speed, important for evaluating the operational efficiency of machinery.")
    color: Optional[str] = Field(None,
                                 description="Indicates the color of the product, which can be relevant for aesthetic considerations or brand identity.")


class ProductCriteria25(AbstractStructure):
    dimensions: Optional[str] = Field(None,
                                      description="Indicates the physical dimensions of the product, ensuring compatibility with other components and the intended application.")
    material: Optional[str] = Field(None,
                                    description="Specifies the type of material used, which affects performance, durability, strength, and resistance to environmental factors.")
    load_capacity: Optional[str] = Field(None,
                                         description="Represents the maximum load the product can handle safely, crucial for applications involving heavy loads.")
    weight: Optional[str] = Field(None,
                                  description="Specifies the weight of the product, which influences handling, installation, and usability, as well as structural integrity.")
    safety_factor: Optional[str] = Field(None,
                                         description="Indicates the reliability and safety of the product under load, with higher values suggesting a more robust design.")
    quantity: Optional[str] = Field(None,
                                    description="Indicates the number of units available or included, relevant for inventory management and procurement.")
    type: Optional[str] = Field(None,
                                description="Specifies the type of product, helping differentiate between various applications and providing context for its design.")
    clamping_width: Optional[str] = Field(None,
                                          description="Indicates the width available for clamping, important for products requiring secure fastening during use.")
    clamping_depth: Optional[str] = Field(None,
                                          description="Indicates the depth available for clamping, ensuring stability and secure attachment during operation.")
    voltage: Optional[str] = Field(None,
                                   description="Specifies the voltage requirements for electrically powered products, crucial for compatibility with power sources.")
    power: Optional[str] = Field(None,
                                 description="Represents the power rating, essential for understanding energy consumption and performance of the product.")
    thread_diameter: Optional[str] = Field(None,
                                           description="Indicates the diameter of the thread, relevant for threaded connections to ensure compatibility and secure assembly.")
    pitch: Optional[str] = Field(None,
                                 description="Specifies the pitch of the thread, crucial for ensuring compatibility and performance in threaded assemblies.")


class ProductCriteria30(AbstractStructure):
    weight: Optional[str] = Field(None,
                                  description="A crucial parameter for understanding portability and application. Heavier components may indicate durability, while lighter ones suggest ease of handling.")
    dimensions: Optional[str] = Field(None,
                                      description="Essential for compatibility with other components and fitting within designated spaces. Ensure dimensions are measured in meters (SI units).")
    voltage: Optional[str] = Field(None,
                                   description="Critical for electrical components. Voltage affects performance and compatibility with power sources. Ensure voltage is measured in volts (SI units).")
    current: Optional[str] = Field(None,
                                   description="Important for evaluating electrical efficiency and safety. Current helps in understanding the product's power requirements. Ensure current is measured in amperes (SI units).")
    diameter: Optional[str] = Field(None,
                                    description="Relevant for cylindrical components, affecting how they fit with other parts. Ensure diameter is measured in meters (SI units).")
    material: Optional[str] = Field(None,
                                    description="Indicates the material used, which impacts durability, weight, and suitability for different environments.")
    category: Optional[str] = Field(None,
                                    description="Helps classify the product based on its intended use and market.")
    type: Optional[str] = Field(None,
                                description="Specifies the product's function and application, crucial for proper evaluation.")
    length: Optional[str] = Field(None,
                                  description="Important for compatibility with other components. Ensure length is measured in meters (SI units).")
    thickness: Optional[str] = Field(None,
                                     description="Relevant for components where strength and durability are key considerations. Ensure thickness is measured in meters (SI units).")
    grade: Optional[str] = Field(None,
                                 description="Indicates the quality or classification of the material, important for performance and reliability.")
    power: Optional[str] = Field(None,
                                 description="For electrical products, power ratings are essential to understand the product's capabilities. Ensure power is measured in watts (SI units).")


class ProductCriteria26(AbstractStructure):
    type: Optional[str] = Field(None,
                                description="Defines the function and application of the product, such as relays or transistors. Different types have distinct characteristics and use cases.")
    voltage: Optional[str] = Field(None,
                                   description="Key parameter for electrical components, determining operational limits and compatibility with other devices. Ensure voltage is measured in volts (SI units).")
    current: Optional[str] = Field(None,
                                   description="Essential for handling the required electrical load safely. Helps evaluate whether the product can operate under the necessary conditions. Ensure current is measured in amperes (SI units).")
    weight: Optional[str] = Field(None,
                                  description="Important for shipping, installation, and handling, especially in larger systems. Ensure weight is measured in kilograms (SI units).")
    dimensions: Optional[str] = Field(None,
                                      description="Crucial for fitting within electronic assemblies or systems. Ensure dimensions are measured in meters (SI units).")
    category: Optional[str] = Field(None,
                                    description="Helps identify the intended use and market segment for the product, influencing purchasing decisions.")
    accuracy_class: Optional[str] = Field(None,
                                          description="Vital for products requiring precision, such as measuring instruments. Indicates the reliability and accuracy of performance.")
    diameter: Optional[str] = Field(None,
                                    description="Relevant for components that need to fit specific connectors or interfaces. Ensure diameter is measured in meters (SI units).")
    power: Optional[str] = Field(None,
                                 description="Critical for understanding the energy consumption and operational capacity of the product. Ensure power is measured in watts (SI units).")
    marking: Optional[str] = Field(None,
                                   description="Provides essential information about the product's specifications and compliance with industry standards.")
    capacity: Optional[str] = Field(None,
                                    description="Crucial for storage devices, indicating the product's ability to store data or energy.")
    interface: Optional[str] = Field(None,
                                     description="Specifies the type of connection or communication with other devices, like USB or other interfaces.")
    rotation_speed: Optional[str] = Field(None,
                                          description="Relevant for rotating components, such as hard drives, affecting performance and efficiency. Ensure speed is measured in revolutions per minute (RPM).")


class ProductCriteria22(AbstractStructure):
    size: Optional[str] = Field(None,
                                description="A crucial parameter that directly affects the compatibility of the tire with various vehicle types. Ensure size measurements are in meters (SI units).")
    diameter: Optional[str] = Field(None,
                                    description="Essential for ensuring proper fit and performance of the tire. Diameter influences handling and stability. Ensure measurements are in meters (SI units).")
    load_index: Optional[str] = Field(None,
                                      description="Indicates the maximum load a tire can carry, critical for safety and performance, especially for commercial vehicles.")
    ply_rating: Optional[str] = Field(None,
                                      description="Reflects the strength and durability of the tire. Higher ply ratings typically indicate tires suited for heavy-duty applications.")
    pressure: Optional[str] = Field(None,
                                    description="Critical for safety, fuel efficiency, and tire longevity. Proper pressure ensures optimal performance. Ensure pressure is measured in pascals (SI units).")
    thickness: Optional[str] = Field(None,
                                     description="Affects the tire’s durability and puncture resistance. Ensure thickness is measured in meters (SI units).")
    type: Optional[str] = Field(None,
                                description="Defines the tire’s suitability for different weather conditions and driving scenarios, such as summer, winter, or all-season tires.")
    color: Optional[str] = Field(None,
                                 description="While not a performance metric, color can influence consumer preferences and branding in the tire market.")
    temperature_range: Optional[str] = Field(None,
                                             description="Indicates the operational limits of the tire, which is crucial for performance in extreme temperature conditions. Ensure temperature is measured in Celsius or Kelvin (SI units).")
    dimensions: Optional[str] = Field(None,
                                      description="Overall dimensions provide a comprehensive understanding of the tire's size and fitment for vehicle compatibility. Ensure dimensions are measured in meters (SI units).")


class ProductCriteria29(AbstractStructure):
    category: Optional[str] = Field(None,
                                    description="Defines the specific type of product and its intended use. Helps in categorizing products for different applications or standards.")
    power: Optional[str] = Field(None,
                                 description="Indicates the performance capability of the electrical equipment. Ensure power is measured in watts (SI units).")
    length: Optional[str] = Field(None,
                                  description="Critical for ensuring compatibility in applications where size matters. Ensure length is measured in meters (SI units).")
    size: Optional[str] = Field(None,
                                description="Important for fitting products into designated spaces and ensuring usability. Ensure size is measured in meters (SI units).")
    diameter: Optional[str] = Field(None,
                                    description="Essential for compatibility in fittings and connections. Ensure diameter is measured in meters (SI units).")
    completeness: Optional[str] = Field(None,
                                        description="Indicates whether the product comes with all necessary components or accessories, important for customer satisfaction.")
    volume: Optional[str] = Field(None,
                                  description="Relevant for products where capacity or space considerations are important. Ensure volume is measured in cubic meters (SI units).")
    color: Optional[str] = Field(None,
                                 description="Primarily an aesthetic consideration, but can influence customer preferences, especially for branding.")
    type: Optional[str] = Field(None,
                                description="Helps in understanding the specific application and function of the product.")
    signs_of_difference: Optional[str] = Field(None,
                                               description="Highlights unique features or certifications that may set the product apart from competitors.")


class ProductCriteria20(AbstractStructure):
    color: Optional[str] = Field(None,
                                 description="Crucial for aesthetic and branding purposes, color can significantly influence consumer preferences and market differentiation.")
    volume: Optional[str] = Field(None,
                                  description="A key metric, especially for liquids or materials where quantity is essential for pricing and usage. Ensure volume is measured in cubic meters (SI units).")
    weight: Optional[str] = Field(None,
                                  description="Important for shipping, handling, and consumer perception of value. Heavier products may be perceived as more substantial or higher quality. Ensure weight is measured in kilograms (SI units).")
    category: Optional[str] = Field(None,
                                    description="Helps in understanding the product's specific use or market segment. Provides context for the intended application of the product.")
    type: Optional[str] = Field(None,
                                description="Provides insight into the product's function and differentiates it from others in the same category, helping consumers identify the right product for their needs.")
    parameters: Optional[str] = Field(None,
                                      description="Refers to additional specifications that may be relevant for specialized markets or technical products. Could provide insights that are not immediately visible.")
    marking: Optional[str] = Field(None,
                                   description="Indicates branding or specific product lines, which can be important for consumer recognition and trust.")
    form: Optional[str] = Field(None,
                                description="Describes the physical form of the product (e.g., gel, liquid), which can influence consumer choice based on application and ease of use.")
    application: Optional[str] = Field(None,
                                       description="Describes the intended use of the product, crucial for consumers to understand how to utilize it effectively.")


class ProductCriteria31(AbstractStructure):
    dimensions: Optional[str] = Field(None,
                                      description="Critical for understanding the size and fit of the furniture in a given space. Ensure dimensions are measured in meters (SI units).")
    material: Optional[str] = Field(None,
                                    description="Essential for evaluating the quality, durability, and aesthetic appeal of the furniture. Different materials affect longevity and maintenance.")
    color: Optional[str] = Field(None,
                                 description="Important for aesthetic considerations. The color can influence the decor and atmosphere of the room.")
    height: Optional[str] = Field(None,
                                  description="Key dimension for understanding the product’s vertical proportions. Ensure height is measured in meters (SI units).")
    width: Optional[str] = Field(None,
                                 description="Key dimension for understanding the product’s horizontal proportions. Ensure width is measured in meters (SI units).")
    length: Optional[str] = Field(None,
                                  description="Key for understanding the product’s length and how it fits into a designated space. Ensure length is measured in meters (SI units).")
    shelves: Optional[str] = Field(None,
                                   description="Indicates the number or presence of shelves, important for assessing functionality and storage capacity.")
    capacity: Optional[str] = Field(None,
                                    description="Relevant for products designed to hold or store items, helping consumers understand how much the furniture can accommodate.")
    emission_class: Optional[str] = Field(None,
                                          description="Important for environmentally conscious consumers. Indicates the level of harmful emissions from the materials used.")
    weight: Optional[str] = Field(None,
                                  description="Relevant for understanding the sturdiness and stability of the furniture. Weight also affects logistics and transport. Ensure weight is measured in kilograms (SI units).")
    edge_material: Optional[str] = Field(None,
                                         description="Affects the durability and finish of the furniture, especially in high-traffic areas where wear and tear are a concern.")


class ProductCriteria32(AbstractStructure):
    length: Optional[str] = Field(None,
                                  description="A critical parameter for determining the size and fit of products. Length affects usability and compatibility with other items. Ensure length is measured in meters (SI units).")
    weight: Optional[str] = Field(None,
                                  description="Influences handling, transportation, and perceived quality of the products. Heavier items may indicate sturdiness and better quality. Ensure weight is measured in kilograms (SI units).")
    color: Optional[str] = Field(None,
                                 description="A significant aesthetic factor that influences consumer choice, helping to differentiate products within the same category.")
    dimensions: Optional[str] = Field(None,
                                      description="Encompasses various measurements, essential for understanding the overall size and shape of the products. Crucial for ensuring fit and meeting specific requirements. Ensure dimensions are measured in meters (SI units).")
    diameter: Optional[str] = Field(None,
                                    description="Particularly relevant for cylindrical products or components, affecting compatibility and functionality. Ensure diameter is measured in meters (SI units).")
    category: Optional[str] = Field(None,
                                    description="Provides context about the intended use and market segment of the products. It helps to evaluate the appropriateness of the product for specific applications.")
    material: Optional[str] = Field(None,
                                    description="The material used affects the durability, appearance, and performance of the products, making it crucial for assessing quality and suitability for different uses.")
    type: Optional[str] = Field(None,
                                description="Helps differentiate between various functionalities and applications of the products, providing clarity on the specific use cases.")
    tensile_strength: Optional[str] = Field(None,
                                            description="Crucial for evaluating the durability and performance of products under stress. It is particularly relevant for tools and items designed to withstand significant forces.")
    breaking_strength: Optional[str] = Field(None,
                                             description="Indicates the limit of the product under load, essential for ensuring safety and reliability in use. This parameter is especially important for tools and components under stress.")


class ProductCriteria23(AbstractStructure):
    diameter: Optional[str] = Field(None,
                                    description="Crucial for products like pipes or rods, where diameter affects flow rates and structural integrity. Ensure diameter is measured in meters (SI units).")
    thickness: Optional[str] = Field(None,
                                     description="Important for assessing the strength and durability of materials, especially in load-bearing applications. Ensure thickness is measured in meters (SI units).")
    dimensions: Optional[str] = Field(None,
                                      description="The overall size of the product, essential for fitting and compatibility in construction projects. Ensure dimensions are measured in meters (SI units).")
    concrete_grade: Optional[str] = Field(None,
                                          description="Indicates the quality and strength of the concrete, which is vital for structural applications.")
    reinforcement: Optional[str] = Field(None,
                                         description="Specifies the type of reinforcement used in concrete products, critical for their strength and stability.")
    weight: Optional[str] = Field(None,
                                  description="Important for logistics, handling, and structural calculations. Ensure weight is measured in kilograms (SI units).")
    grit: Optional[str] = Field(None,
                                description="Relevant for products requiring specific texture or surface finishing, impacting adhesion and performance.")
    temperature_range: Optional[str] = Field(None,
                                             description="Indicates the environmental conditions the product can withstand, critical for outdoor applications. Ensure temperature is measured in Celsius or Kelvin (SI units).")
    material: Optional[str] = Field(None,
                                    description="The type of material used, such as reinforced concrete, affects durability, strength, and suitability for specific applications.")
    quantity: Optional[str] = Field(None,
                                    description="Important for inventory management and project planning, ensuring sufficient materials are available for the project.")
    color: Optional[str] = Field(None,
                                 description="While less critical than structural parameters, color can be relevant for aesthetic considerations in visible applications.")
    size: Optional[str] = Field(None,
                                description="Provides information on the product’s scale and usability in specific contexts, similar to dimensions.")


class ProductCriteria58(AbstractStructure):
    pages: Optional[str] = Field(None,
                                 description="A critical parameter for evaluating printed materials, as the number of pages indicates the depth and comprehensiveness of the content.")
    year: Optional[str] = Field(None,
                                description="Indicates the year of publication, important for assessing the relevance and timeliness of the material. Newer publications may contain more current information.")
    dimensions: Optional[str] = Field(None,
                                      description="Relevant for understanding the physical size of the product, which affects usability, storage, and display. Ensure dimensions are measured in meters (SI units).")
    weight: Optional[str] = Field(None,
                                  description="Important for shipping, handling, and logistics, especially in bulk orders. Ensure weight is measured in kilograms (SI units).")
    material: Optional[str] = Field(None,
                                    description="Indicates the quality and durability of the printed material, impacting the overall customer experience.")
    size: Optional[str] = Field(None,
                                description="Relevant for categorizing the product and understanding its intended use (e.g., A3 size).")
    category: Optional[str] = Field(None,
                                    description="Helps identify the type of product and its target audience, essential for marketing and sales strategies.")
    protection_system: Optional[str] = Field(None,
                                             description="Relevant for products that require security features, such as digital formats needing access protection.")
    safety_mark: Optional[str] = Field(None,
                                       description="Important for products that must meet certain safety standards, ensuring compliance and consumer trust.")
    resolution: Optional[str] = Field(None,
                                      description="Relevant for printed materials that include images or graphics, as it affects the quality and clarity of the print.")
    frequency: Optional[str] = Field(None,
                                     description="Indicates how often the product is published, which is critical for subscription-based products.")


class ProductCriteria17(AbstractStructure):
    format: Optional[str] = Field(None,
                                  description="Essential for categorizing paper products. Different formats (e.g., A4, A5) affect usability and compatibility with other office supplies.")
    size: Optional[str] = Field(None,
                                description="Critical for determining compatibility with storage solutions and office supplies. Ensure size is measured in meters (SI units).")
    pages: Optional[str] = Field(None,
                                 description="Important for products like folders and notebooks, as the number of pages directly relates to capacity and usability.")
    weight: Optional[str] = Field(None,
                                  description="Important for assessing paper quality, affecting durability and printability. Ensure weight is measured in grams per square meter (gsm).")
    color: Optional[str] = Field(None,
                                 description="A significant differentiator that influences aesthetic appeal and branding of paper products.")
    type: Optional[str] = Field(None,
                                description="Defines the type of paper product (e.g., folder, sheet), which is fundamental for understanding its intended use and market positioning.")
    capacity: Optional[str] = Field(None,
                                    description="Crucial for folders, indicating how many sheets the product can hold, helping consumers find specific storage solutions.")
    paper_type: Optional[str] = Field(None,
                                      description="Indicates the type of paper (e.g., offset, glossy), affecting the product’s application and quality.")
    mechanism: Optional[str] = Field(None,
                                     description="For folders, the mechanism (e.g., ring binder) is essential for functionality and user experience.")
    whiteness: Optional[str] = Field(None,
                                     description="Indicates the quality of the paper, particularly important for printing applications.")
    gloss: Optional[str] = Field(None,
                                 description="Affects the visual quality of printed materials, relevant for products where appearance is a key factor.")
    embossing: Optional[str] = Field(None,
                                     description="Enhances the aesthetic appeal of products, particularly in premium paper offerings.")
    volume: Optional[str] = Field(None,
                                  description="Relevant for products sold in bulk or those requiring storage, indicating the overall capacity or quantity.")


class ProductCriteria15(AbstractStructure):
    size: Optional[str] = Field(None,
                                description="A critical factor for proper fit and comfort in protective footwear. Ensuring correct sizing is essential for safety and performance.")
    color: Optional[str] = Field(None,
                                 description="While secondary to functional attributes, color can play a role in aesthetic appeal and consumer choice.")
    material: Optional[str] = Field(None,
                                    description="The type of material (e.g., leather, microfiber) affects durability, comfort, and protection level, crucial for evaluating the footwear’s quality.")
    sole_type: Optional[str] = Field(None,
                                     description="Important for traction and stability, especially in hazardous work conditions. Different sole types provide varying levels of grip and durability.")
    toe_protection: Optional[str] = Field(None,
                                          description="Vital for safety, especially in environments where foot injuries are a risk. Metal or composite toe protection is a key differentiator among products.")
    additional_features: Optional[str] = Field(None,
                                               description="Includes safety features such as puncture protection and oil resistance, enhancing the footwear’s suitability for specific work environments.")
    climate_zones: Optional[str] = Field(None,
                                         description="Indicates the footwear’s suitability for various environmental conditions, ensuring protection in different climates.")
    energy_absorption: Optional[str] = Field(None,
                                             description="Crucial for protective footwear in industrial settings, where energy absorption helps mitigate the impact of heavy objects.")
    compression_resistance: Optional[str] = Field(None,
                                                  description="Indicates the footwear’s ability to withstand compression, ensuring safety in environments where heavy loads are present.")
    purpose: Optional[str] = Field(None,
                                   description="Helps consumers select the right footwear for specific tasks, whether for general protection or specialized applications.")
    thickness: Optional[str] = Field(None,
                                     description="Relates to the durability and insulation properties of the footwear, which are important for comfort and protection in various conditions.")


class ProductCriteria10(AbstractStructure):
    weight: Optional[str] = Field(None,
                                  description="A fundamental characteristic for food products, influencing serving sizes, pricing, and nutritional content. Ensure weight is measured in kilograms (SI units).")
    fat_content: Optional[str] = Field(None,
                                       description="Essential for health-conscious consumers and regulatory standards, helping to evaluate the nutritional profile of the products.")
    category: Optional[str] = Field(None,
                                    description="Vital for classifying food products and understanding consumer expectations in different market segments.")
    type: Optional[str] = Field(None,
                                description="Important for identifying the product's characteristics and positioning in the market. Helps differentiate between types such as cured sausage or grain-based products.")
    marking: Optional[str] = Field(None,
                                   description="Indicates branding and quality assurance, playing a role in consumer trust and product differentiation.")
    volume: Optional[str] = Field(None,
                                  description="Relevant for understanding the quantity of product offered, especially important for liquids. Ensure volume is measured in liters (SI units).")


class ProductCriteria24(AbstractStructure):
    dimensions: Optional[str] = Field(None,
                                      description="Critical for ensuring proper fit and functionality. Dimensions such as length, width, thickness, and diameter are fundamental for product compatibility in specific applications.")
    material: Optional[str] = Field(None,
                                    description="Determines the product's strength, durability, and suitability for various environments. The type of material used (e.g., steel, copper) is a key differentiator.")
    pressure: Optional[str] = Field(None,
                                    description="Indicates the maximum pressure the product can withstand, essential for safety and performance in applications involving fluids or gases.")
    color: Optional[str] = Field(None,
                                 description="Affects aesthetic appeal and product identification. Color can also be important for distinguishing different product types.")
    size: Optional[str] = Field(None,
                                description="Important for compatibility with other components or systems, ensuring the product fits within specific design requirements.")
    type: Optional[str] = Field(None,
                                description="Helps in identifying the intended use and application of the product, such as specific fittings or components.")
    thread_type: Optional[str] = Field(None,
                                       description="Critical for ensuring proper connections and assembly, especially in products that involve fittings.")
    regulations: Optional[str] = Field(None,
                                       description="Ensures compliance with industry standards and regulations (e.g., ГОСТ), vital for ensuring product safety and quality.")
    temperature_range: Optional[str] = Field(None,
                                             description="Indicates the operational limits of the product, crucial for applications in varying environmental conditions.")
    marking: Optional[str] = Field(None,
                                   description="Provides important information about the product's specifications and compliance, useful for ensuring the product meets relevant standards.")


class ProductCriteria13(AbstractStructure):
    dimensions: Optional[str] = Field(None,
                                      description="Defines the physical size of the products, which is essential for fitting and usability in various applications. Ensure dimensions are measured in meters (SI units).")
    color: Optional[str] = Field(None,
                                 description="A significant aesthetic factor that can influence consumer choice, especially in textile products where appearance is key.")
    material: Optional[str] = Field(None,
                                    description="The type of material used affects durability, comfort, and maintenance of the products, which is crucial for their intended use and quality.")
    size: Optional[str] = Field(None,
                                description="Important for practical applications and consumer preferences, especially in textiles where fit can be critical.")
    category: Optional[str] = Field(None,
                                    description="Helps in positioning the product within the market and identifying the target customer segment.")
    weight: Optional[str] = Field(None,
                                  description="Relevant for shipping, handling, and usability, especially for larger textile products. Ensure weight is measured in kilograms (SI units).")
    type: Optional[str] = Field(None,
                                description="Helps differentiate between various product forms and uses, which is essential for marketing and consumer understanding.")
    standards: Optional[str] = Field(None,
                                     description="Compliance with industry standards ensures quality assurance and builds consumer trust.")
    features: Optional[str] = Field(None,
                                    description="Specific features such as antibacterial properties or fire resistance can add value to the products, making them more appealing.")
    closure_type: Optional[str] = Field(None,
                                        description="Relevant for products requiring secure fastening, impacting functionality and usability.")


class ProductCriteria16(AbstractStructure):
    dimensions: Optional[str] = Field(None,
                                      description="Crucial for understanding the size and fit of the product, especially in construction and design applications. Ensure dimensions are measured in meters (SI units).")
    material: Optional[str] = Field(None,
                                    description="The type of material, such as different wood types (e.g., pine, larch), affecting durability, appearance, and suitability for specific applications.")
    grade: Optional[str] = Field(None,
                                 description="Indicates the quality and suitability for various applications, with higher grades typically representing better quality and fewer defects.")
    width: Optional[str] = Field(None,
                                 description="Important for determining how the product will fit into a specific space or application. Ensure width is measured in meters (SI units).")
    height: Optional[str] = Field(None,
                                  description="Similar to width, height is a critical dimension affecting the product's usability and application. Ensure height is measured in meters (SI units).")
    length: Optional[str] = Field(None,
                                  description="An essential dimension that impacts the application and usability of the product. Ensure length is measured in meters (SI units).")
    color: Optional[str] = Field(None,
                                 description="While less frequently mentioned, color can play a significant role in aesthetic considerations for design and construction.")
    thickness: Optional[str] = Field(None,
                                     description="Influences the strength and durability of the product, making it relevant for various applications. Ensure thickness is measured in meters (SI units).")
    depth: Optional[str] = Field(None,
                                 description="Important for certain applications where the depth of the product impacts its functionality, particularly in construction.")
    slat_width: Optional[str] = Field(None,
                                      description="Relevant for products that involve slats or panels. Ensure slat width is measured in meters (SI units).")
    slat_thickness: Optional[str] = Field(None,
                                          description="Indicates the thickness of slats, influencing strength and durability. Ensure slat thickness is measured in meters (SI units).")
    quantity: Optional[str] = Field(None,
                                    description="Important for bulk purchasing decisions and project planning, indicating the available quantity of the product.")
    category: Optional[str] = Field(None,
                                    description="Helps in identifying the type and intended use of the product, essential for proper evaluation.")
    light_transmission: Optional[str] = Field(None,
                                              description="Relevant for products used in applications where light filtering is important, such as windows or screens.")


class ProductCriteria11(AbstractStructure):
    volume: Optional[str] = Field(None,
                                  description="Most critical parameter for pricing and consumer choice. Different volumes cater to various consumer needs. Ensure volume is measured in liters (SI units).")
    alcohol_content: Optional[str] = Field(None,
                                           description="Essential for alcoholic beverages, informing consumers about the strength of the drink. Important for legal compliance and health considerations. Ensure alcohol content is measured in percentage (%).")
    type: Optional[str] = Field(None,
                                description="Key differentiator for consumer preferences, indicating the kind of beverage (e.g., sparkling, still, dry).")
    packaging: Optional[str] = Field(None,
                                     description="Influences convenience and sustainability, important for consumer preferences. Packaging type can impact purchasing decisions.")
    category: Optional[str] = Field(None,
                                    description="Helps classify the product (e.g., mineral water, whiskey), which is important for marketing and consumer recognition.")
    brand: Optional[str] = Field(None,
                                 description="Affects consumer trust and loyalty, especially in competitive markets. Brand recognition can strongly influence purchasing decisions.")
    marking: Optional[str] = Field(None,
                                   description="Provides additional product information, such as specific features or quality indicators, relevant for consumer trust.")
    weight: Optional[str] = Field(None,
                                  description="Relevant for shipping and handling considerations, especially for larger quantities. Ensure weight is measured in kilograms (SI units).")
    variety: Optional[str] = Field(None,
                                   description="Important for products like wines, where different varieties appeal to specific consumer tastes.")
    series: Optional[str] = Field(None,
                                  description="Indicates a specific product line from a brand, which can influence consumer loyalty and brand recognition.")


class ProductCriteria21(AbstractStructure):
    weight: Optional[str] = Field(None,
                                  description="Crucial for dosage accuracy and product handling. Weight can also influence shipping costs and storage requirements. Ensure weight is measured in grams (SI units).")
    volume: Optional[str] = Field(None,
                                  description="Essential for understanding the amount of product provided, directly affecting dosage and usage. Ensure volume is measured in milliliters or liters (SI units).")
    concentration: Optional[str] = Field(None,
                                         description="Vital for determining the potency of the product, particularly important in pharmaceuticals. Ensure concentration is provided in appropriate units (e.g., mg/mL).")
    quantity: Optional[str] = Field(None,
                                    description="Indicates how many units are included in the packaging, important for inventory management and consumer purchasing decisions.")
    dosage: Optional[str] = Field(None,
                                  description="Critical for ensuring the product is used safely and effectively, especially in medical or pharmaceutical applications.")
    type: Optional[str] = Field(None,
                                description="Helps categorize the product and informs users about its intended use, crucial for proper application.")
    dimensions: Optional[str] = Field(None,
                                      description="Affects packaging and storage, and may also influence the application method for certain products. Ensure dimensions are measured in meters (SI units).")
    form: Optional[str] = Field(None,
                                description="Indicates the physical form of the product (e.g., cream, powder), influencing user preference and application method.")
    packaging: Optional[str] = Field(None,
                                     description="Important for product protection, shelf life, and user convenience.")
    category: Optional[str] = Field(None,
                                    description="Helps classify the product within the broader market, which is useful for regulatory and marketing purposes.")


class ProductCriteria19(AbstractStructure):
    type: Optional[str] = Field(None,
                                description="Defines the specific application of the oil (e.g., transmission, motor, hydraulic). It is a primary criterion for understanding the oil's purpose and suitability.")
    category: Optional[str] = Field(None,
                                    description="Provides insight into the oil's intended use and market segment, helping consumers understand the product’s suitability for their needs.")
    viscosity: Optional[str] = Field(None,
                                     description="A key characteristic affecting the oil’s performance under different temperature conditions. Ensures compatibility with engine specifications and operational efficiency.")
    marking: Optional[str] = Field(None,
                                   description="Indicates the brand and specific product line, which can influence consumer choice based on reputation and perceived quality.")
    regulations: Optional[str] = Field(None,
                                       description="Ensures compliance with industry standards and regulations, crucial for safety and performance.")
    temperature_range: Optional[str] = Field(None,
                                             description="Indicates the operational limits of the oil, important for avoiding product failure in extreme conditions. Ensure temperature is measured in Celsius or Kelvin (SI units).")
    seasonality: Optional[str] = Field(None,
                                       description="Helps understand whether the oil is suitable for all seasons or specific conditions, guiding consumer choice based on climate.")
    api_rating: Optional[str] = Field(None,
                                      description="The American Petroleum Institute (API) rating provides a standardized measure of oil quality and performance, making it significant for evaluation.")
    brand: Optional[str] = Field(None,
                                 description="While not as critical as technical specifications, brand reputation can influence consumer trust and purchasing decisions.")


class ProductCriteria01(AbstractStructure):
    category: Optional[str] = Field(None,
                                    description="Defines the type of product (e.g., flowers, vegetables, decorative plants). Understanding the category helps identify the target market and potential uses.")
    weight: Optional[str] = Field(None,
                                  description="Significant for logistics, pricing, and customer expectations. Influences shipping costs and handling requirements. Ensure weight is measured in kilograms (SI units).")
    height: Optional[str] = Field(None,
                                  description="Important for determining the suitability of plants for different environments (e.g., indoor vs. outdoor) and customer preferences. Ensure height is measured in meters (SI units).")
    marking: Optional[str] = Field(None,
                                   description="Provides specific identification for the products, essential for branding and customer recognition, and may indicate quality or specific varieties.")
    type: Optional[str] = Field(None,
                                description="Helps differentiate between various subcategories within the main category, providing insights into specific characteristics and uses of the products.")
    parameters: Optional[str] = Field(None,
                                      description="Additional specifications or features of the product, which can be important for customers seeking specific attributes.")
    composition: Optional[str] = Field(None,
                                       description="For plants, knowing the composition informs customers about the variety and quality, which is vital for horticultural products.")
    tray_dimensions: Optional[str] = Field(None,
                                           description="Relevant for understanding how the products are packaged and displayed, which can affect sales and customer satisfaction. Ensure tray dimensions are measured in meters (SI units).")
    volume: Optional[str] = Field(None,
                                  description="Relevant for understanding the size of the product offering, especially in bulk sales. Ensure volume is measured in liters or cubic meters (SI units).")
    color: Optional[str] = Field(None,
                                 description="A significant factor in customer choice, especially for decorative plants and flowers.")
    completeness: Optional[str] = Field(None,
                                        description="Indicates whether the product is sold as a complete set or if additional items are needed, which can affect customer satisfaction.")
    signs_of_difference: Optional[str] = Field(None,
                                               description="Unique features that set the product apart from others, which can serve as a key selling point.")
