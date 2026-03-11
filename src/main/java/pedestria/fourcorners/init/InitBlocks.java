package pedestria.fourcorners.init;

import java.util.ArrayList;
import java.util.List;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import pedestria.fourcorners.blocks.AvaliteOreBlock;
import pedestria.fourcorners.blocks.BlocksBase;
import pedestria.fourcorners.blocks.CoreFabricatorBlockSimple;
import pedestria.fourcorners.blocks.WisdomOreBlock;

public class InitBlocks {

	public static final List<Block> BLOCKS = new ArrayList<Block>();
	// Ores
	public static final Block AVALITE_ORE_BLOCK = new AvaliteOreBlock("avalite_ore_block", Material.ROCK,InitItems.AVALON_GEM);
	public static final Block WISDOM_ORE_BLOCK = new WisdomOreBlock("wisdom_ore_block", Material.ROCK,InitItems.WISDOM_SHARD);

	// Machines
	public static final Block DIMENSION_ACCESSOR_BLOCK = new BlocksBase("dimension_accessor_block", Material.IRON);
	public static final Block SIMPLE_CORE_FABRICATOR = new CoreFabricatorBlockSimple("core_fabricator_simple_block",Material.IRON);

}
