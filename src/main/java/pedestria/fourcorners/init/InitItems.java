package pedestria.fourcorners.init;

import java.util.ArrayList;
import java.util.List;

import net.minecraft.item.Item;
import pedestria.fourcorners.items.ItemsBase;

public class InitItems 
{
	public static final List<Item> ITEMS = new ArrayList<Item>();
	
	//List of all items.
	public static final Item START_TOME = new ItemsBase("start_tome"); //The Grand Tome of Knowledge
	public static final Item WISDOM_SHARD =  new ItemsBase("wisdom_shard"), AVALON_GEM = new ItemsBase("avalon_gem");;	// Wisdom Shard
	//public static final Item AVALON_CORE = new ItemsBase("avalon_core"); 
	
	// Registered Ingots
	public static final Item WISDOM_INGOT = new ItemsBase("wisdom_ingot");
	public static final Item AVALON_INGOT = new ItemsBase("avalon_ingot");
	
}
