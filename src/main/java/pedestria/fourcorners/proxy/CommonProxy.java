package pedestria.fourcorners.proxy;

import net.minecraft.item.Item;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.fml.common.registry.GameRegistry;
import net.minecraftforge.oredict.OreDictionary;
import pedestria.fourcorners.init.InitBlocks;
import pedestria.fourcorners.init.InitItems;
import pedestria.fourcorners.tiles.TileEntityCoreFabricatorSimple;

public class CommonProxy 
{
	public void registerItemRenderer(Item item,int meta,String id) {}

	
	public void registerOreDict () 
	{
		OreDictionary.registerOre("oreAvalite", InitBlocks.AVALITE_ORE_BLOCK);
		OreDictionary.registerOre("gemAvalon", InitItems.AVALON_GEM);
		
		OreDictionary.registerOre("oreWisdom", InitBlocks.WISDOM_ORE_BLOCK);
		OreDictionary.registerOre("shardWisdom", InitItems.WISDOM_SHARD);
		OreDictionary.registerOre("dustWisdom", InitItems.WISDOM_SHARD);
		
		OreDictionary.registerOre("ingotAvalon",InitItems.AVALON_INGOT);
		OreDictionary.registerOre("ingotWisdom",InitItems.WISDOM_INGOT);
		
	}
	
	public static void initTileEntities () 
	{
		GameRegistry.registerTileEntity(TileEntityCoreFabricatorSimple.class, new ResourceLocation("fourcorners:tile_entity_core_fabricator_simple"));
	}
}
